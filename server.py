import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the host and port
    host = '127.0.0.1'  # Localhost
    port = 65432        # Port to listen on

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Enable the server to accept connections
    server_socket.listen()

    
    while True:
        # Accept a connection from a client
        client_socket, addr = server_socket.accept()
        print(f"\nServer")

        while True:
            try:
                # Receive data from the client
                data = client_socket.recv(1024)
                
                if not data:
                    print("Client disconnected.")
                    break  # Exit the loop if no data is received (client disconnected)
                print(f"{data.decode()}")

                # Echo the data back to the client
                client_socket.sendall(data)

            except ConnectionResetError:
                print("Connection closed by the client.")
                break  # Exit the loop if the connection was closed abruptly

        client_socket.close()

if __name__ == "__main__":
    start_server()
