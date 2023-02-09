# Python UDP Client

This is a basic implementation of a UDP client in Python, using the `socket` module. The client listens for incoming messages at the IP address `127.0.0.1` and port `25005`.

## Usage

The `start_client` function creates a new UDP socket, binds it to the specified IP address and port, and enters an infinite loop to receive incoming messages. For each incoming message, the function prints the received data to the console.

If the script is run as the main module, the `start_client` function is called to start the UDP client.

## Note

This code is just an example of a basic UDP client, and does not include error handling or robustness features that would be required in a production environment. The code is sourced from the [Python UDP Communication](https://wiki.python.org/moin/UdpCommunication) page on the Python wiki.

## Limitations

The maximum message size that can be received by the client, as defined by the BUFFER_SIZE constant, is 1024 bytes. If a message larger than this size is sent, it will be truncated to fit within the buffer, and only the first 1024 bytes of the message will be received and processed by the client.

If multiple apps try to send messages at the same time, the order in which the messages are received by the client is not guaranteed. It is possible for messages to arrive out of order, or for messages to be lost or duplicated. To ensure reliable communication, it may be necessary to implement a higher-level protocol on top of the basic UDP communication, such as adding message sequencing or error correction.

## Error handling

In order to ensure that the client continues to listen for incoming messages even in case of errors, the code contains `try-except` blocks that handle exceptions raised by the `socket` module. If an error occurs while receiving a message, the code inside the `except` blocks will handle it and the `while` loop will continue, allowing the client to continue receiving messages.
