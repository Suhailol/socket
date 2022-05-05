import socket
HOST = socket.gethostname()
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    data = sock.recv(1024)
    print("Current Time from server = ", data.decode())

