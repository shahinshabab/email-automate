# debug_companies.py
from database import get_connection

conn = get_connection()
cur = conn.cursor()

for row in cur.execute("SELECT email, company FROM recipients LIMIT 20;"):
    print(dict(row))

conn.close()
