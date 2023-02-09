"""
Python UDP client. Source: https://wiki.python.org/moin/UdpCommunication
"""
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 25005
BUFFER_SIZE = 1024


def start_client():
    sock = socket.socket(
        socket.AF_INET,  # Internet
        socket.SOCK_DGRAM,  # UDP
    )
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Listening on port {UDP_PORT}")

    while True:
        try:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            print(f"Received message: {data}")
        except socket.timeout as e:
            print(f"Timeout occurred while receiving data: {e}")
        except socket.error as e:
            print(f"Error occurred while receiving data: {e}")


if __name__ == "__main__":
    start_client()
