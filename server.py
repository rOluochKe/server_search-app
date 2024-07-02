import socket
import threading
import ssl
import configparser
import os
import time
import sys

# Constants
MAX_PAYLOAD_SIZE: int = 1024
ROOT_DIR: str = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE: str = os.path.join(ROOT_DIR, 'config.ini')


class Server:
    """A class representing a TCP server."""

    def __init__(self, port: int) -> None:
        """Initialize the Server instance with the given port."""
        self.port = port
        self.load_config()
        self.load_file()
        self.bind_socket()
        self.run()

    def load_config(self) -> None:
        """Load configuration settings from the config file."""
        config: configparser.ConfigParser = configparser.ConfigParser()
        config.read(CONFIG_FILE)
        self.linux_path: str = config.get('Server', 'linuxpath', fallback='')
        self.reread_on_query: bool = config.getboolean(
            'Server', 'reread_on_query', fallback=False)
        self.ssl_enabled: bool = config.getboolean(
            'SSL', 'enabled', fallback=False)
        self.ssl_certfile: str = config.get('SSL', 'certfile', fallback='')
        self.ssl_keyfile: str = config.get('SSL', 'keyfile', fallback='')

    def load_file(self) -> None:
        """Load file content from the specified path."""
        self.file_content: str = ""
        print("Attempting to load file from:", self.linux_path)  # Debug print
        if os.path.exists(self.linux_path):
            with open(self.linux_path, 'r') as file:
                self.file_content = file.read()
            print("File loaded successfully.")
        else:
            print("File not found at the specified path.")

    def bind_socket(self) -> None:
        """Bind the server socket and configure SSL if enabled."""
        self.server_socket: socket.socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', self.port))
        self.server_socket.listen(5)

        if self.ssl_enabled:
            self.server_socket = ssl.wrap_socket(self.server_socket,
                                                 certfile=self.ssl_certfile,
                                                 keyfile=self.ssl_keyfile,
                                                 server_side=True)

    def linear_search(self, query: str) -> bool:
        """
        Search for a row in the file content using linear search.

        Args:
        - query (str): The row to search for in the file content.

        Returns:
        - bool: True if the row exists in the file content, False otherwise.
        """
        try:
            query = query.strip()  # Remove leading/trailing whitespace
            for line in self.file_content.split('\n'):
                if query == line.strip():
                    return True  # Row exists in the file content
            return False  # Row not found in the file content
        except Exception as e:
            print(f"Error: {e}")
            raise e

    def handle_client(self, client_socket: socket.socket,
                      address: str) -> None:
        """Handle client requests."""
        while True:
            try:
                data: bytes = client_socket.recv(
                    MAX_PAYLOAD_SIZE).rstrip(b'\x00')
                if not data:
                    break
                start_time: float = time.time()
                # Remove leading/trailing whitespace
                query = data.decode('utf-8').strip()
                if self.reread_on_query:
                    self.load_file()  # Reload file content if needed
                found = self.linear_search(query)
                if found:
                    response: str = "STRING EXISTS\n"
                else:
                    response: str = "STRING NOT FOUND\n"
                client_socket.send(response.encode('utf-8'))
                execution_time: float = time.time() - start_time
                print(
                    f"DEBUG: Query: {query}, IP: {address}, + Execution Time: {execution_time}"
                )
            except Exception as e:
                print(f"Error: {e}")
                break
        client_socket.close()

    def run(self) -> None:
        """Start the server and handle incoming client connections."""
        print(f"Server is running on port {self.port}...")
        try:
            while True:
                client_socket, address = self.server_socket.accept()
                print(f"Connection from {address} has been established!")
                client_thread = threading.Thread(
                    target=self.handle_client, args=(client_socket,
                                                     str(address)))
                client_thread.start()
        except KeyboardInterrupt:
            print("Exiting the server...")
            self.server_socket.close()
            sys.exit()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)
    port: int = int(sys.argv[1])
    server: Server = Server(port)
