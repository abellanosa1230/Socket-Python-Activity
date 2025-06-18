import socket

# Convert an integer to network byte order (big-endian)
def int_to_network_byte_order(value):
    return socket.htonl(value)  # htonl: host to network long (32-bit)

# Convert an integer from network byte order to host byte order
def network_byte_order_to_int(value):
    return socket.ntohl(value)  # ntohl: network to host long (32-bit)

# Usage 
if __name__ == "__main__":
    original_value = 123456789

    print(f"Original Value: {original_value}")

    # Convert to network byte order
    network_value = int_to_network_byte_order(original_value)
    print(f"Network Byte Order Value: {network_value}")

    # Convert back to host byte order
    host_value = network_byte_order_to_int(network_value)
    print(f"Back to Host Byte Order: {host_value}")
