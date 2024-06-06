#firewall_solution = secrettoken
import socket

def connect_to_server(ip, port):
    try:
        
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        client_socket.connect((ip, port))
        print(f"Connected to server at {ip}:{port}")
        
        
        message = "Hello, Server!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent message: {message}")
        
       
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Received response: {response}")
        
        #
        client_socket.close()
        print("Connection closed")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    ip = "12.169.91.135"
    port = 8080
    connect_to_server(ip, port)
