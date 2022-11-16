import socket


def main():
    host = socket.gethostname()
    port = 8000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(5)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    connection, address = server_socket.accept()

    while True:
        message_from_client = connection.recv(256).decode()

        if not message_from_client or message_from_client == "exit":
            break

        print(f'Отримано повідомлення від клієнта: "{message_from_client}"')

        message = input('>> ').lower()
        connection.send(message.encode())

        if message_from_client == "exit":
            break

    connection.close()


if __name__ == '__main__':
    main()

