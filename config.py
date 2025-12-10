# config.py
import os
from pathlib import Path
from dotenv import load_dotenv  # NEW

BASE_DIR = Path(__file__).resolve().parent

# Load .env from the same directory as this file
load_dotenv(BASE_DIR / ".env")

# SQLite DB file (same path on laptop & EC2)
DB_PATH = BASE_DIR / "email_automation.db"

# --- AWS credentials (taken from .env) ---
AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
AWS_SES_SENDER = os.getenv("AWS_SES_SENDER", "shahin@shahinanalytics.com")

# These are optional: boto3 will also pick them up directly from environment
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_SESSION_TOKEN = os.getenv("AWS_SESSION_TOKEN")  # only if you use temporary creds

# Sending controls
DAILY_LIMIT = int(os.getenv("DAILY_LIMIT", "80"))
DELAY_SECONDS = float(os.getenv("DELAY_SECONDS", "5"))

# Safety flag for testing
DRY_RUN = os.getenv("DRY_RUN", "true").lower() == "true"

# Which campaign/wave is this run?
CAMPAIGN_NAME = os.getenv("CAMPAIGN_NAME", "initial")