import MySQLdb

db = MySQLdb.connect(host="localhost", user="", passwd="", db="")
cur = db.cursor()

name = raw_input('Enter name: ')

# sql injection
cur.execute("SELECT * FROM users WHERE name = %s;" % name)

for row in cur.fetchall():
  print(row)

db.close()
