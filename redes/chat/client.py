import socket
import threading


class Client:
    def __init__(self, host="localhost", port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def receive_messages(self):
        while True:
            data = self.client_socket.recv(1024).decode()
            if not data:
                break
            print(f"Recibido del servidor: {data}")

    def send_messages(self):
        while True:
            message = input("Escriba un mensaje para enviar al servidor: ")
            self.client_socket.send(message.encode())

    def start(self):
        self.client_socket.connect((self.host, self.port))
        threading.Thread(target=self.receive_messages).start()
        self.send_messages()


if __name__ == "__main__":
    client = Client()
    client.start()
