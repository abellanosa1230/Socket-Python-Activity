import socket

# Define the server IP and port
HOST = '127.0.0.1'
PORT = 12345

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Define the name to send to the server (embedded)
name = "MIAHLYN ABELLANOSA"

# Send the name to the server
client_socket.send(name.encode())

# Receive the server's response
response = client_socket.recv(1024).decode()
print("Received from server:", response)

# Close the client socket
client_socket.close()
