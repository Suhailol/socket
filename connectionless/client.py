import socket
from turtle import hideturtle
HOST = socket.gethostname()
PORT = 5050
addr = (HOST, PORT)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    msg = "hi"
    s.sendto(msg.encode(), addr)
    tm = s.recv(1024)
    print(tm.decode())
