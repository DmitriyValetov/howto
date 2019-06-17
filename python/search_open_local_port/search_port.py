from contextlib import closing
import socket


def find_open_ports():
    for port in range(5000, 8081):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            res = sock.connect_ex(('localhost', port))
            if res == 0:
                yield port

def port_free(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        res = sock.connect_ex(('localhost', port))
        if res == 0:
            return True
    return False


if __name__ == "__main__":
    port_generator = find_open_ports() 
    print(next(port_generator))