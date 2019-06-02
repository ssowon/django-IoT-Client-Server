# client1
import sys, socket
import serial
import datetime
import sqlite3
port = "/dev/ttyACM0"       # 아두이노 포트 : ttyACM0
ser = serial.Serial(port, 9600)
ser.flushInput()

def echo_client(server_addr):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(server_addr)
	print('connected: ', sock.getpeername())
	while True:
		message = sys.stdin.readline()
		if message == '\n': # enter를 칠 때
			ser.write("in".encode('utf-8')) #아두이노에게 광센서의 센서 값 입력 받기 위해서 in을 보냄
			light = int(ser.readline())     # 값 받아오기
			s_msg = "type:load\r\ntime:%s\r\ncds:%s\r\n" %(datetime.datetime.now(), light) #시간과 센서 값 첨부해서 서버로 문자열 보냄
			sock.send(s_msg.encode('utf-8'))
		data = sock.recv(1024).decode('utf-8')
		print(data, end='')
	sock.close()

if __name__ == '__main__':
	echo_client(('192.168.0.33', 30303)) ## 서버의 IP주소와 팀원끼리 임의로 정한 포트번호