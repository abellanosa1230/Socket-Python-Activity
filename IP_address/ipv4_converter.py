# Converts each octet of the IPv4 address to 8-bit binary and joins them with dots
def ipv4_to_binary(ip):
    return '.'.join(f"{int(octet):08b}" for octet in ip.split('.'))

# Converts each octet of the IPv4 address to 3-digit octal and joins them with dots
def ipv4_to_octal(ip):
    return '.'.join(f"{int(octet):03o}" for octet in ip.split('.'))

# Converts each octet of the IPv4 address to 2-digit uppercase hexadecimal and joins them with dots
def ipv4_to_hex(ip):
    return '.'.join(f"{int(octet):02X}" for octet in ip.split('.'))

# Converts the IPv4 address to a single 32-bit integer
def ipv4_to_integer(ip):
    parts = [int(octet) for octet in ip.split('.')]  # Split IP into 4 parts and convert to integers
    return (parts[0] << 24) + (parts[1] << 16) + (parts[2] << 8) + parts[3]  # Combine into 32-bit int

# Calls all the conversion functions and prints the results
def convert_ipv4(ip):
    print(f"Original IPv4 Address: {ip}")
    print(f"Binary Format        : {ipv4_to_binary(ip)}")
    print(f"Octal Format         : {ipv4_to_octal(ip)}")
    print(f"Hexadecimal Format   : {ipv4_to_hex(ip)}")
    print(f"Integer Format       : {ipv4_to_integer(ip)}")

# Script is run directly 
if __name__ == "__main__":
    ip_address = "192.168.1.1"  
    convert_ipv4(ip_address)
