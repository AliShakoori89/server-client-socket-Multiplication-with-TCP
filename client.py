import socket
import sys
 
# Create a TCP/IP socket
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# Define host
host = '127.0.0.1'
 
# define the communication port
port = 12345
 
# Connect the socket to the port where the server is listening
server_address = ((host, port))
 
print ("connecting")
 
stream_socket.connect(server_address)
 
 
# Send data
message1 = input("number 1 : ")
message2 = input('number 2 : ')
#s.send(message.encode())
stream_socket.sendall(message1.encode())
stream_socket.sendall(message2.encode())
 
# response
data = stream_socket.recv(10)
print (data)