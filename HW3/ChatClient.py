import socket
import threading

def receive_messages(s):
    while True:
        try:
            msg = s.recv(1024).decode()
            if msg:
                print(msg)
            else:
                break
        except:
            print("An error occurred!")
            #s.close()
            break

def main(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            receiver = threading.Thread(target=receive_messages, args=(s,))
            receiver.daemon = True
            receiver.start()
            
            name = input("")
            s.send(name.encode())

            while True:
                try:
                    msg = input()
                    s.send(msg.encode())
                except EOFError:
                    break
        except KeyboardInterrupt:
            print("\nExiting Chat...")
        finally:
            s.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python ChatClient.py <port number>")
        sys.exit()
    host = "localhost"
    port = int(sys.argv[1])
    main(host, port)
