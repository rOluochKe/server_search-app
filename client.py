import socket
import sys


def main() -> None:
    """Main function to run the client."""
    server_ip: str = 'localhost'
    try:
        port: int = int(input("Enter server port: "))
        while True:
            query: str = input("Enter search query (or 'exit' to quit): ")
            if query.lower() == 'exit':
                print("\nExiting the client...")
                break
            try:
                with socket.socket(socket.AF_INET,
                                   socket.SOCK_STREAM) as client_socket:
                    client_socket.connect((server_ip, port))
                    client_socket.send(query.encode('utf-8'))
                    response: str = client_socket.recv(1024).decode('utf-8')
                    print(response)
            except Exception as e:
                print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nExiting the client...")
        sys.exit()


if __name__ == "__main__":
    main()
