import sqlite3 as sql

# connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

# Drop company table if already exsist.
cur.execute("DROP TABLE IF EXISTS company")

# Create Company table  in db_web database
sql ='''CREATE TABLE "company" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"CNAME"	TEXT,
	"EMAIL" TEXT,
	"CONTACT"	TEXT,
	"ADDRESS" TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()

