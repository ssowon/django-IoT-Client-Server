import sqlite3

conn=sqlite3.connect('light.sqlite3')
c=conn.cursor()

for row in c.execute('SELECT * FROM LIGHT'):
	print(row)
