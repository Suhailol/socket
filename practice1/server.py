import socket
PORT = 5051
HOST = socket.gethostname()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            print("Client: ", data.decode())
            data = input('Enter a message to the client')
            if not data:
                break
            # data = input('Enter a message to the client')
            conn.sendall(bytearray(data, "utf-8"))
    conn.close()