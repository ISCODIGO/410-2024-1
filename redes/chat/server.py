import socket
import threading


class Server:
    def __init__(self, host="localhost", port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))

    def handle_client(self, client_socket):
        while True:
            received_data = client_socket.recv(1024).decode()
            if not received_data:
                break
            print(f"Recibido del cliente: {received_data}")

            message = input("Escriba un mensaje para enviar al cliente: ")
            client_socket.send(message.encode())

        client_socket.close()

    def start(self):
        self.server_socket.listen(1)
        print("Servidor esperando conexiones...")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Conexión desde {client_address} ha sido establecida.")

            client_handler = threading.Thread(
                target=self.handle_client, args=(client_socket,)
            )
            client_handler.start()


if __name__ == "__main__":
    server = Server()
    server.start()
