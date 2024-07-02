# Multithreaded TCP Server-Client Search Application

## Project Overview

This project implements a multithreaded TCP server and client for searching content within a text file. The server is designed to handle multiple client connections concurrently.

## Features

- <b>Multithreaded Server:</b> Efficiently handles concurrent client requests using Python's threading module.
- <b>TCP Communication:</b> Establishes reliable connections between server and clients using TCP sockets.
- <b>File Search:</b> Enables clients to search for specific lines (rows) within the server's loaded text file.
- <b>Configuration:</b> Loads server settings from a configuration file (`config.ini`).
- <b>Error Handling:</b> Catches and reports exceptions for robust operation.
- <b>Testing:</b> Includes unit tests using `pytest` for code verification.

## Setup

1. <b>Prerequisites:</b> Ensure you have Python 3 and pip installed.

2. <b>Dependencies:</b> Install required packages using `pip install -r requirements.txt`.

3. <b>Configuration File (config.ini):</b> Create a config.ini file in the project directory with the following structure:

    ```
    [Server]
    linuxpath=path/to/your/file.txt   ; Path to the text file for searching
    reread_on_query=True                ; Whether to reload file content on each client query (optional)

    [SSL]
    enabled=False                      ; Enable SSL encryption (optional)
    certfile=server.crt                 ; Path to server certificate file (if SSL enabled)
    keyfile=server.key                  ; Path to server key file (if SSL enabled)
    ```
4. <b>Text File:</b> Prepare your text file (`200k.txt` in this example) containing the searchable content.

## Running

### Server:

- Open a terminal in the project directory.
- Start the server using: `python server.py <port_number>` (e.g., `python server.py 8080`).
- The server will print confirmation messages indicating it's running on the specified port.

### Client(s):

- In separate terminal windows, run: `python client.py`
- Enter the server's port number when prompted (e.g., 8080 if you used port 8080 for the server).
- Type search queries, separated by Enter.
- The client will display responses indicating whether the string was found or not.
- Type `exit` and press Enter to quit.

## Examples

### Server:

  ```
  Server is running on port 8080...
  Connection from ('127.0.0.1', 54321) has been established!
  DEBUG: Query: line1, IP: 127.0.0.1, Execution Time: 0.000123
  Connection from ('127.0.0.1', 54322) has been established!
  DEBUG: Query: line3, IP: 127.0.0.1, Execution Time: 0.000234
  ... (more connections and queries)
  Exiting the server...
  ```

### Client:
  ```
  Enter server port: 8080
  Enter search query (or 'exit' to quit): line1
  STRING EXISTS

  Enter search query (or 'exit' to quit): line_not_found
  STRING NOT FOUND

  Enter search query (or 'exit' to quit): exit

  Exiting the client...
  ```

### Testing

The project includes unit tests using pytest. To run the tests:

- Open a terminal in the project directory.
- Run: `pytest`

## Explanation

### Server (server.py)

- `Server class`: Handles server initialization, configuration loading, file handling, TCP socket operations, and client connections using threads.
- `load_config`: Reads server settings from `config.ini`.
- `load_file`: Loads the text file content.
- `bind_socket`: Creates the server socket and wraps it with SSL if enabled.
- `linear_search`: Performs a linear search for the query string within the loaded file content.
- `handle_client`: Runs in a separate thread for each client, receiving search queries, performing search, and sending responses.
- `run`: Starts the server loop, listening for incoming connections, spawning client threads, and handling `KeyboardInterrupt`  for graceful termination.

## Multithreading

The server leverages Python's threading module to handle multiple client connections concurrently. This enhances scalability and responsiveness by allowing the server to process requests from different clients without blocking.

### Client Threading (`server.py`)

- `handle_client`: This method is the heart of multithreading. It's invoked within a separate thread for each client connection. This enables the server to serve multiple clients simultaneously without waiting for one client's request-response cycle to complete before attending to another client.
- <b>Thread Creation:</b> Inside the server's `run` method, when a new client connection is established using `server_socket.accept()`, a new thread is created using `threading.Thread(target=self.handle_client, args=(client_socket, address))`.
- <b>Thread Target:</b> The `target` argument specifies the function to be executed within the thread, which in this case is `self.handle_client`.
- <b>Thread Arguments:</b> The `args` argument is a tuple containing arguments to be passed to the target function. Here, it provides the connected client socket and its IP address to the `handle_client` method.
- <b>Thread Start:</b> By calling `client_thread.start()`, the thread is instructed to begin execution, allowing it to handle the specific client's communication independently.

### Benefits of Multithreading

- <b>Improved Performance:</b> The server can handle multiple client requests concurrently, reducing overall response times and improving responsiveness under heavy client load.
- <b>Efficient Resource Utilization:</b> Threads are lightweight compared to processes, allowing the server to make better use of system resources (CPU, memory) by servicing clients in parallel.
- <b>Scalability:</b> The server's ability to handle concurrent client connections scales gracefully as the number of clients increases.

### Limitations of Multithreading

<b>Complexity:</b> Threading can introduce additional complexity to the code, requiring careful design and synchronization mechanisms to avoid race conditions and deadlocks.
<b>Shared Resources:</b> Access to shared resources (like the loaded file content) needs proper synchronization to ensure data consistency when multiple threads access the same data.
