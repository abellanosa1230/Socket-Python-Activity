import socket

# Define the IP address and port for the server
HOST = '127.0.0.1'
PORT = 12345

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow address reuse so the server can restart quickly after closing
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the address and port
server_socket.bind((HOST, PORT))

# Enable the server to accept connections (1 = max queue of 1 client)
server_socket.listen(1)
print("Server is listening...")

# Accept a connection from a client
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from the client
data = conn.recv(1024).decode()
print("Received from client:", data)

# Send a response back to the client with the embedded name
response = data
conn.send(response.encode())

# Close the connection
conn.close()
server_socket.close()

