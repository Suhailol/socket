import socket
HOST = socket.gethostname()
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    s_name, addr = s.recvfrom(1024)
    s_name = s_name.decode()
    print(s_name, " has entered your chat!")
    name = input("Enter your name: ")
    s.sendto(name.encode("ascii"), addr)
    while True:
        message = input("Me: ")
        s.sendto(message.encode(), addr)
        message, addr = s.recvfrom(1024)
        message = message.decode()
        print(s_name, ": ", message)
