import socket
from http.client import HTTPConnection

if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 3345))
        s.sendall(b"Hello, world")
        data = s.recv(1024)
        print(data)
