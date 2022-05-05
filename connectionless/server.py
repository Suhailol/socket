import socket
import time
HOST = socket.gethostname()
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    
    while True:
        data, addr = s.recvfrom(1024)
        currentTime = time.ctime(time.time()) + "\r\n"
        s.sendto(currentTime.encode('ascii'), addr)

