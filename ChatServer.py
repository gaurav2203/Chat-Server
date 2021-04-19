import socket
import threading
import datetime

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_ip= input("Enter the IP of your system:")
s_port= input("Enter the port number:")
s.bind((s_ip, int(s_port)))

r= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
r_ip= input("Enter the IP of other system:")
r_port=int(input("Enter the port number:"))

def time():
    t= str(datetime.datetime.now())
    t= t.split(' ')[1][:5]
    return t

def send():
    while 1:
        msg= input()
        s.sendto( msg.encode(), (r_ip, r_port))
        print('_'*(40) + time())
        print("")

def receive():
    while 1:
        buffer_size= 1024
        msg= s.recvfrom(buffer_size)
        print('[' +r_ip + ']' + ' ' + msg[0].decode())
        print('_'*(40) + time())
        print("")

receiveThread= threading.Thread(target= receive)
sendThread= threading.Thread(target= send)

receiveThread.start()
sendThread.start()
