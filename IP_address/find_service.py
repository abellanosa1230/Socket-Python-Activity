import socket

def get_service_name(port, protocol):

    try:
        # Ensure the protocol is in lowercase for comparison
        protocol = protocol.lower()

        # Use socket to get the service name from the system
        service_name = socket.getservbyport(port, protocol)
        return service_name
    except OSError as e:
        return f"Error: {e}"

def main():
    # Input: Port and Protocol (tcp/udp)
    port = int(input("Enter port number: "))
    protocol = input("Enter protocol (tcp/udp): ").strip().lower()

    # Ensure protocol is valid
    if protocol not in ['tcp', 'udp']:
        print("Error: Protocol must be 'tcp' or 'udp'.")
        return

    # Get the service name
    service_name = get_service_name(port, protocol)

    if service_name.startswith("Error"):
        print(service_name)
    else:
        print(f"The service name for port {port} and protocol {protocol} is: {service_name}")

if __name__ == "__main__":
    main()
