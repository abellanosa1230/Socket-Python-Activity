import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get default send and receive buffer sizes
default_send_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
default_recv_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

print("Default Send Buffer Size:", default_send_buf)
print("Default Receive Buffer Size:", default_recv_buf)

# Set new buffer sizes (in bytes)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)  # 4 KB send buffer
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 8192)  # 8 KB receive buffer

# Verify new buffer sizes
new_send_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
new_recv_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)

print("Modified Send Buffer Size:", new_send_buf)
print("Modified Receive Buffer Size:", new_recv_buf)

# Close the socket
sock.close()
