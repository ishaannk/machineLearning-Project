import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="PAH#84#jeor",
    database="college",
    port=3306
)

print("✅ DB Connected Successfully")
conn.close()
