# Retrieving a Remote Machine's IP Address

import socket

# Get the hostname (user input)
remote_host = input("Enter the hostname: ")

try:
    # Get the IP address using socket.gethostbyname
    remote_ip = socket.gethostbyname(remote_host)
    print(f"IP address {remote_ip}")

except socket.error:
    print("There was an error resolving the hostname. Please check the input.")
