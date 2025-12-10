# import_csv.py

import csv
from pathlib import Path
from database import get_connection

# ---------------------------------------------------------
# You ONLY change this value:
CSV_FILENAME = "recipients.csv"
# ---------------------------------------------------------

# Automatically resolve the CSV path in the SAME directory
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / CSV_FILENAME


def import_csv(csv_path: Path):
    """
    Import recipients from a CSV located in the same directory.

    Expected columns (any of these variants are accepted):
    - Email address, email
    - First name, first_name
    - Last name, last_name
    - Organization, Domain name, Input domain name
    """

    if not csv_path.exists():
        print(f"[ERROR] CSV file not found: {csv_path}")
        return

    conn = get_connection()
    cur = conn.cursor()

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        imported = 0
        skipped_duplicates = 0

        for row in reader:

            # -------- Email (required) --------
            email = (
                row.get("Email address")
                or row.get("email")
                or row.get("Email")
                or ""
            ).strip()

            if not email:
                continue  # Skip rows without email

            # -------- Names --------
            first_name = (
                row.get("First name")
                or row.get("first_name")
                or row.get("First")
                or ""
            ).strip()

            last_name = (
                row.get("Last name")
                or row.get("last_name")
                or row.get("Last")
                or ""
            ).strip()

            # -------- Company / Organization --------
            company = (
                row.get("Organization")
                or row.get("Domain name")
                or row.get("Input domain name")
                or ""
            ).strip()

            # No custom template in CSV (handled in email builder)
            custom_subject = None
            custom_body = None

            # -------- Check duplicate email --------
            cur.execute("SELECT id FROM recipients WHERE email = ?", (email,))
            exists = cur.fetchone()

            if exists:
                skipped_duplicates += 1
                continue

            # -------- Insert new recipient --------
            cur.execute(
                """
                INSERT INTO recipients
                    (email, first_name, last_name, company, custom_subject, custom_body)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (email, first_name, last_name, company, custom_subject, custom_body),
            )
            imported += 1

    conn.commit()
    conn.close()

    print("------------------------------------------------")
    print(f"CSV Loaded:         {csv_path.name}")
    print(f"New recipients:     {imported}")
    print(f"Duplicates skipped: {skipped_duplicates}")
    print("------------------------------------------------")


if __name__ == "__main__":
    import_csv(CSV_PATH)
