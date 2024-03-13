from xmlrpc.server import SimpleXMLRPCServer
import os

class MyServer:
    def __init__(self):
        self.messages = []

    def sort_list(self, nums):
        return sorted(nums)
    
    def print_message(self, msg):
        print(msg)
        self.messages.append(msg)
        return self.messages

    def get_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                return file.read()
        except Exception as e:
            print(f'Error: {e}')
            return False
def main():
    server = MyServer()
    with SimpleXMLRPCServer(('localhost', 8000), allow_none=True) as rpc_server:
        print("Listening on port 8000...")
        rpc_server.register_instance(server)
        rpc_server.serve_forever()

if __name__ == "__main__":
    main()
