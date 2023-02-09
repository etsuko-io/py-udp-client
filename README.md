# Python UDP Client

This is a basic implementation of a UDP client in Python, using the `socket` module. The client listens for incoming messages at the IP address `127.0.0.1` and port `25005`.

## Usage

The `start_client` function creates a new UDP socket, binds it to the specified IP address and port, and enters an infinite loop to receive incoming messages. For each incoming message, the function prints the received data to the console.

If the script is run as the main module, the `start_client` function is called to start the UDP client.

## Note

This code is just an example of a basic UDP client, and does not include error handling or robustness features that would be required in a production environment. The code is sourced from the [Python UDP Communication](https://wiki.python.org/moin/UdpCommunication) page on the Python wiki.
