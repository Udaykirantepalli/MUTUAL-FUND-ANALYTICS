import sqlite3

conn = sqlite3.connect("bluestock_mf.db")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM fact_nav")
print("fact_nav rows:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM fact_transactions")
print("fact_transactions rows:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(*) FROM fact_performance")
print("fact_performance rows:", cursor.fetchone()[0])

conn.close()