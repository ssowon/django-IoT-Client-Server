import sys
from socket import socket, AF_INET, SOCK_STREAM
import time
import re
import sqlite3

def echo_server(my_port):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(('192.168.0.33', my_port)) # '' 안에 서버의 아이피값을 입력합니다.
	sock.listen(5)
	print('server started')
	while True:
		conn, cli_addr = sock.accept()
		print('connected by', cli_addr)
		try:
			while True:
				data = conn.recv(1024)
				if not data: break
				print('server received', data.decode())
				r_msg=data.decode()
				s=r_msg.split()
				db = sqlite3.connect('light.db')
				cursor = db.cursor()

				# data type load
				if(s[0][5:]=='load'):
					datein=(s[1][5:]+" "+s[2])[:19]
					cds = s[3][:]
					cursor.execute("INSERT INTO LIGHT VALUES(?, ?);",(datein, cds))
					db.commit()
					msg="server received by client\n"
					conn.send(msg.encode())

				# data type get
				elif(s[0][5:]=='get'):
					dateget = s[1][5:]+" "+s[2]
					intable=False
					for row in cursor.execute('SELECT * FROM LIGHT'):
						if dateget == row[0]:
							msg="client founded by serverDB {0}\n".format(row[1])
							conn.send(msg.encode())
							intable=True
					if intable==False :
						conn.send("wrong\n".encode())
				db.close()

		# Exception Handling
		except OSError as e:
			print('socket error: ', e)
		except Exception as e:
			print('exception: ',e)
		else:
			print('client closed', cli_addr)
		finally:
			conn.close()


if __name__ == '__main__':
	echo_server(30303)
