import socket

# Specify the server's host name and port
host = 'localhost'
port = 3000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Prepare the HTTP GET request command
request = 'GET / HTTP/1.0\r\nHost: localhost\r\n\r\n'

# Send the request to the server
client_socket.send(request.encode())

while True:
    datos = client_socket.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end="")

# Close the socket
client_socket.close()
