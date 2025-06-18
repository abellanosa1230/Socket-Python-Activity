import socket

def connect_to_server(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Connecting to {host}: {port}")
        
        # Try to connect
        sock.connect((host, port))
        print("Connected successfully!")

        # Send a simple message
        message = "Hello, Server!"
        sock.sendall(message.encode())
        
        # Receive response
        response = sock.recv(1024)
        print("Server response:", response.decode())

    except socket.error:
        print("Error connecting to server.")
    
    except socket.error as e:
        print(f"Socket error: {e}")
    
    except Exception as ex:
        print(f"General error: {ex}")
    
    finally:
        # Ensure socket is closed
        sock.close()
        print("Socket closed.")

# Try connecting to a non-listening server (to force an error)
connect_to_server("localhost", 9999)
