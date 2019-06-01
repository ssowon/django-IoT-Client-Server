import sys, socket

def echo_client(server_addr):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(server_addr)
	print('connected: ', sock.getpeername())
	while True:
		message = sys.stdin.readline() # 광센서의 값을 알고싶은 시간 보내기 ex) 2019-05-13 15:40:12
		if message :
			msg = "type:get\r\ntime:{0}\r\n".format(message) # 메세지를 type:get\n\ntime:2019-05-13 15:40:12 이런 식으로 보냄
			sock.send(msg.encode('utf-8')) # 원하는 시간의 메세지를 서버에 보낸다.
		data = sock.recv(1024).decode('utf-8') # 서버에서 "client founded by serverDB"라는 메세지를 보내면 값을 받는다.
		print(data)
	sock.close()

if __name__ == '__main__':
	echo_client(('192.168.0.33', 30303)) # 서버의 IP주소와 팀원끼리 임의로 정한 포트 번호