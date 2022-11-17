import socket
import threading

port_c = 12345
port_s = 54321
ip = '127.0.0.1'
max_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip, port_c))
s.connect((ip, port_s))

name = input("Enter your username: ")

def receive():
    while 1:
        message_r = s.recv(max_size)
        print("\t\t"+ message_r.decode())

def send():
    while 1:
        message_s = input("Enter your message: ")
        s.send((name + ': ' + message_s).encode())

threads = []
t1 = threading.Thread(target=receive)
threads.append(t1)
t2 = threading.Thread(target=send)
threads.append(t2)
for t in threads:
    t.setDaemon(True)
    t.start()
    
t.join()
s.close()