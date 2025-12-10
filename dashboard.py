# dashboard.py
import datetime as dt

import pandas as pd
import streamlit as st

from database import get_connection


def load_data(start_date: dt.date, end_date: dt.date) -> pd.DataFrame:
    conn = get_connection()
    query = """
        SELECT
            sl.batch_date,
            sl.status AS send_status,
            sl.message_id,
            sl.error,
            r.email,
            r.first_name,
            r.last_name,
            r.company,
            r.custom_subject,
            r.sent_at
        FROM send_log sl
        JOIN recipients r ON r.id = sl.recipient_id
        WHERE sl.batch_date BETWEEN ? AND ?
        ORDER BY sl.batch_date DESC, sl.id DESC
    """
    df = pd.read_sql_query(
        query,
        conn,
        params=(start_date.isoformat(), end_date.isoformat()),
    )
    conn.close()
    return df


def main():
    st.title("Email Sending Dashboard (SES + SQLite)")
    today = dt.date.today()
    default_start = today - dt.timedelta(days=7)

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start date", value=default_start, max_value=today)
    with col2:
        end_date = st.date_input("End date", value=today, max_value=today)

    if start_date > end_date:
        st.error("Start date cannot be after end date.")
        return

    df = load_data(start_date, end_date)

    if df.empty:
        st.info("No send logs for this period.")
        return

    # Summary metrics
    total_sent = (df["send_status"] == "sent").sum()
    total_failed = (df["send_status"] == "failed").sum()
    unique_recipients = df["email"].nunique()

    st.subheader("Summary")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total sent", total_sent)
    c2.metric("Total failed", total_failed)
    c3.metric("Unique recipients", unique_recipients)

    st.subheader("Details")
    st.dataframe(df)

if __name__ == "__main__":
    main()
