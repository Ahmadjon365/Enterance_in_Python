# SQLite3 lesson
import sqlite3

con = sqlite3.connect("database.db")
cursor = con.cursor()

cursor.execute("""
SELECT * FROM employees LIMIT 5
""")

ans = cursor.fetchall()
# for row in ans:
#     print(row)
print(ans[0])

cursor.close()
con.close()
