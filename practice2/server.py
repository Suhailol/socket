import socket
import time
HOST = socket.gethostname()
PORT = 5050
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()

    with conn:
        print("Connected by ", addr)
        while True:
            currentTime = time.ctime(time.time()) + "\r\n"
            conn.send(currentTime.encode('ascii'))
        conn.close()
