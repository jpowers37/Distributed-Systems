import socket
import threading

def broadcast(message, connection, clients):
    for client in clients:
        if client != connection:
            try:
                client.send(message.encode())
            except:
                client.close()
                remove(client, clients)

def remove(connection, clients):
    if connection in clients:
        clients.remove(connection)

def client_thread(conn, addr, clients):
    name = conn.recv(1024).decode()
    while True:
        try:
            msg = conn.recv(1024).decode()
            if msg:
                broadcast(f"{name}: {msg}", conn, clients)
            else:
                remove(conn, clients)
                break
        except:
            continue

def main(port):
    host = "localhost"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    clients = []

    try:
        while True:
            conn, addr = server_socket.accept()
            clients.append(conn)
            threading.Thread(target=client_thread, args=(conn, addr, clients)).start()

    except KeyboardInterrupt:
        for client in clients:
            client.close()
        server_socket.close()

        
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ChatServer.py <port number>")
        sys.exit()
    port = int(sys.argv[1])
    main(port)
