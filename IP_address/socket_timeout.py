import socket

# Setting the default socket timeout
socket.setdefaulttimeout(20)  # Set timeout 

# Getting the current default socket timeout
timeout = socket.getdefaulttimeout()

# Print the current timeout setting
print(f"The current default socket timeout: {timeout} seconds")

# Usage of the socket with the default timeout
try:
    # Try connecting to a host (example: converge.com)
    sock = socket.create_connection(('www.convergeict.com', 80)) # This will Raise a timeout if it takes longer than the default timeout
    print("Connection successful!")
except socket.timeout:
    print("Connection timed out.")
except Exception as e:
    print(f"An error occurred: {e}")
