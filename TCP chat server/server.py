import socket
HOST = socket.gethostname()
PORT = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Waiting for connection")
    conn, addr = s.accept()

    with conn:
        s_name = conn.recv(1024)
        s_name = s_name.decode()
        print(s_name, " has entered the chat!")
        name = input(str("Enter your name:"))
        conn.send(name.encode())
        while True:
            # s_name = conn.recv(1024)
            # s_name = s.decode()
            # print(s_name, " has entered the chat!")
            # name = input(str("Enter your name:"))
            # conn.send(name.encode())
            message = input(str("Me: "))
            if message == '[e]':
                message = "Left chat room"
                conn.send(message.encode())
                break
            conn.send(message.encode())
            message = conn.recv(1024)
            message = message.decode()
            print(s_name, ": ", message)

