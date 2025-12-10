# run_daily.py
import time
import datetime as dt

import boto3
from botocore.exceptions import ClientError

from config import (
    DAILY_LIMIT,
    DELAY_SECONDS,
    AWS_REGION,
    AWS_SES_SENDER,
    DRY_RUN,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_SESSION_TOKEN,
)
from database import get_connection
from email_templates import build_subject, build_html_body


def get_today_iso():
    return dt.date.today().isoformat()


def get_already_sent_today(conn, today):
    cur = conn.cursor()
    cur.execute(
        """
        SELECT COUNT(*) AS cnt
        FROM send_log
        WHERE batch_date = ? AND status = 'sent'
        """,
        (today,),
    )
    row = cur.fetchone()
    return row["cnt"] if row else 0


def pick_recipients_to_send(conn, remaining_limit):
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM recipients
        WHERE status = 'pending'
        ORDER BY id
        LIMIT ?
        """,
        (remaining_limit,),
    )
    return cur.fetchall()


def mark_recipient_status(conn, recipient_id, status, error_msg=None):
    cur = conn.cursor()

    if status == "sent":
        cur.execute(
            """
            UPDATE recipients
            SET status = ?, last_error = NULL, sent_at = CURRENT_TIMESTAMP
            WHERE id = ?
            """,
            (status, recipient_id),
        )
    else:
        cur.execute(
            """
            UPDATE recipients
            SET status = ?, last_error = ?
            WHERE id = ?
            """,
            (status, error_msg, recipient_id),
        )

    conn.commit()


def log_send(conn, recipient_id, batch_date, status, message_id=None, error=None):
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO send_log (recipient_id, batch_date, status, message_id, error)
        VALUES (?, ?, ?, ?, ?)
        """,
        (recipient_id, batch_date, status, message_id, error),
    )
    conn.commit()


def send_email_ses(ses_client, sender, recipient_email, subject, html_body):
    response = ses_client.send_email(
        Source=sender,
        Destination={
            "ToAddresses": [recipient_email],
        },
        Message={
            "Subject": {"Data": subject, "Charset": "UTF-8"},
            "Body": {
                "Html": {"Data": html_body, "Charset": "UTF-8"},
            },
        },
    )
    return response["MessageId"]


def build_ses_client():
    """
    Create the SES client using credentials from .env (via config).
    If keys are not set in config, boto3 will fall back to the normal
    environment / shared credentials chain.
    """
    client_kwargs = {"region_name": AWS_REGION}

    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
        client_kwargs.update(
            {
                "aws_access_key_id": AWS_ACCESS_KEY_ID,
                "aws_secret_access_key": AWS_SECRET_ACCESS_KEY,
            }
        )
        if AWS_SESSION_TOKEN:
            client_kwargs["aws_session_token"] = AWS_SESSION_TOKEN

    return boto3.client("ses", **client_kwargs)


def main():
    conn = get_connection()
    today = get_today_iso()

    already_sent = get_already_sent_today(conn, today)
    remaining = max(0, DAILY_LIMIT - already_sent)

    print(f"Today: {today}")
    print(f"Daily limit: {DAILY_LIMIT}, already sent: {already_sent}, remaining: {remaining}")

    if remaining <= 0:
        print("Daily limit reached. Exiting.")
        conn.close()
        return

    recipients = pick_recipients_to_send(conn, remaining)
    if not recipients:
        print("No pending recipients. Exiting.")
        conn.close()
        return

    if DRY_RUN:
        print("DRY_RUN is ON – no real emails will be sent. Just logging.")
        ses_client = None
    else:
        ses_client = build_ses_client()

    for idx, r in enumerate(recipients, start=1):
        # Convert sqlite3.Row -> dict so .get() works in templates
        row = dict(r)

        email = row["email"]
        subject = build_subject(row)
        html_body = build_html_body(row)

        print(f"[{idx}/{len(recipients)}] Sending to {email} ...")

        if DRY_RUN:
            # Simulate success
            message_id = f"dry-run-{email}-{int(time.time())}"
            log_send(conn, row["id"], today, "sent", message_id=message_id, error=None)
            mark_recipient_status(conn, row["id"], "sent")
            print("DRY RUN: marked as sent (no real email).")
        else:
            try:
                message_id = send_email_ses(ses_client, AWS_SES_SENDER, email, subject, html_body)
                log_send(conn, row["id"], today, "sent", message_id=message_id, error=None)
                mark_recipient_status(conn, row["id"], "sent")
                print(f"Sent OK. MessageId={message_id}")
            except ClientError as e:
                err = str(e)
                log_send(conn, row["id"], today, "failed", message_id=None, error=err)
                mark_recipient_status(conn, row["id"], "failed", error_msg=err)
                print(f"FAILED to {email}: {err}")

        # Respect delay between sends
        if idx < len(recipients):
            time.sleep(DELAY_SECONDS)

    conn.close()
    print("Run completed.")


if __name__ == "__main__":
    main()
