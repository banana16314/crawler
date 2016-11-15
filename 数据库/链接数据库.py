import pymysql

conn=pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="0318",
    db="scraping"
    )
cur=conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages")
print (cur.fetchone())
cur.close()
conn.close()
