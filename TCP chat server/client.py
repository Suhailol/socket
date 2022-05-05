import socket
HOST = socket.gethostname()
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    print("Connected")
    name = input(str("Enter your name"))
    sock.send(name.encode())
    s_name = sock.recv(1024)
    s_name = s_name.decode()
    print(s_name," has entered your chat")

    while True:
        message = sock.recv(1024)
        message = message.decode()
        print(s_name, ": ", message)
        message = input(str("Enter a message: "))
        sock.send(message.encode())
        