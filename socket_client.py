import socket


def main():
    host = socket.gethostname()
    port = 8000

    client_socket = socket.socket()

    client_socket.connect((host, port))

    message = input('>> ').lower()

    while message != 'exit':
        client_socket.send(message.encode())
        message_from_server = client_socket.recv(256).decode()
        
        print(f'Отримано повідомлення з сервера: "{message_from_server}"')
        message = input('>> ').lower()

        if message == "exit":
            break

    client_socket.close()


if __name__ == '__main__':
    main()
