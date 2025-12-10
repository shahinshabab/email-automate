# database.py
import sqlite3
from pathlib import Path
from config import DB_PATH

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    # Recipients table: one row per target
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS recipients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            first_name TEXT,
            last_name TEXT,
            company TEXT,
            custom_subject TEXT,
            custom_body TEXT,
            status TEXT NOT NULL DEFAULT 'pending', -- pending/sent/failed
            last_error TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            sent_at TEXT
        );
        """
    )

    # Send log: one row per send attempt
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS send_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recipient_id INTEGER NOT NULL,
            batch_date TEXT NOT NULL, -- YYYY-MM-DD
            status TEXT NOT NULL,     -- sent/failed
            message_id TEXT,
            error TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (recipient_id) REFERENCES recipients(id)
        );
        """
    )

    conn.commit()
    conn.close()
    print(f"DB initialized at {DB_PATH}")

if __name__ == "__main__":
    init_db()
