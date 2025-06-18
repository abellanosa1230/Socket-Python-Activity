import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server address and port
    host = '127.0.0.1'  # Server address
    port = 65432        # Server port

    # Connect to the server
    client_socket.connect((host, port))
    
    print("\nClient")
    
    while True:
        try:
            # Get user input
            message = input(":")
            if message.lower() == 'exit':
                break  # Exit the loop if the user types 'exit'

            # Send the message to the server
            client_socket.sendall(message.encode())

        except KeyboardInterrupt:
            print("\nConnection closed by the client.")
            break  # Gracefully exit on keyboard interrupt

    client_socket.close()

if __name__ == "__main__":
    start_client()
