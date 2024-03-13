import sys, socket, getopt, datetime

def main():
    if sys.argv[1] == '-s': #Server
        host = "localhost"
        if len(sys.argv) < 2:
            print("Usage: Messenger port")
            sys.exit()

        port = int(sys.argv[2])

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                while True:
                    msg = conn.recv(1024)
                    if not msg:
                        break
                    print(str(msg[::-1], "ASCII").strip('\n'))
                conn.close()
    else: #Client
        if len(sys.argv) < 3:
            print("Usage: Messenger host port")
            sys.exit()

        host = sys.argv[2]
        port = int(sys.argv[1])


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            while True:
                try:
                    inp = input()
                    print(inp)
                    s.send((inp + '\n').encode('ASCII'))
                except EOFError:
                    s.shutdown(socket.SHUT_RDWR)
                    s.close()
                    break
                
if __name__ == "__main__":
    main()
