import socket
import sys 

PORT = 50000
BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("connected server")

try:
    client.connect((host, PORT))
except:
    print("error: not connected")
    sys.exit()

msg = input("write message: ")
client.sendall(msg.encode("utf-8"))

data = client.recv(BUFSIZE)
print("message from server: ")
print(data.decode("UTF-8"))

client.close()