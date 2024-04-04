import socket

DOMAIN = "data.pr4e.org"
PORT = 80
URL = "http://data.pr4e.org/romeo.txt"

# Create a socket object
misock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
misock.connect((DOMAIN, PORT))

# Prepare the HTTP GET request command with just the path of the resource, not the full URL
cmd = f"GET {URL} HTTP/1.0\r\n\r\n".encode()

# Send the request to the server
misock.send(cmd)

# Receive the response from the server in a loop
while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(), end="")

# Close the socket
misock.close()
