import sqlite3

conn = sqlite3.connect('light.db')
c = conn.cursor()
c.execute("""CREATE TABLE LIGHT(DATE, LIGHT)""")
conn.commit()
conn.close()
