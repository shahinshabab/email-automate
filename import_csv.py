import csv
from pathlib import Path
from database import get_connection

# ---------------------------------------------------------
# You ONLY change this value:
CSV_FILENAME = "recipients.csv"
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / CSV_FILENAME

# Possible column names for company/organization
COMPANY_HEADERS = [
    "Company",
    "company",
    "Company name",
    "Company Name",
    "Organization",
    "Organization name",
    "Org",
    "Domain name",
    "Input domain name",
    "Domain",
]


def get_first_nonempty(row, keys):
    """Helper: return first non-empty cell from a list of possible header names."""
    for key in keys:
        if key in row and row[key]:
            value = row[key].strip()
            if value:
                return value
    return ""


def import_csv(csv_path: Path):
    """
    Import recipients from a CSV located in the same directory.

    Expected columns (any of these variants are accepted):
    - Email address, email, Email
    - First name, first_name, First
    - Last name, last_name, Last
    - Company / Organization / Domain...
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

        print(f"[INFO] CSV columns: {reader.fieldnames}")

        for row in reader:
            # -------- Email (required) --------
            email = (
                row.get("Email address")
                or row.get("email")
                or row.get("Email")
                or ""
            ).strip()

            if not email:
                continue

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
            company = get_first_nonempty(row, COMPANY_HEADERS)

            if not company:
                # Optional: log once per row so you see which ones are missing
                print(f"[WARN] No company found for {email}")

            custom_subject = None
            custom_body = None

            # -------- Check duplicate email --------
            cur.execute("SELECT id FROM recipients WHERE email = ?", (email,))
            exists = cur.fetchone()

            if exists:
                skipped_duplicates += 1
                continue

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
