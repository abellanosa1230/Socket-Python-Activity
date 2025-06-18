import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Print initial blocking mode (should be True)
print("Initial Blocking Mode:", sock.getblocking())

# Change to non-blocking mode
sock.setblocking(False)
print("Blocking Mode After setblocking:", sock.getblocking())

# Change back to blocking mode
sock.setblocking(True)
print("Blocking Mode After setblocking:", sock.getblocking())

# Clean up
sock.close()
