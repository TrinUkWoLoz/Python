#!/usr/bin/python3

#Script designed to take a URL as a positional argument and return associated IP address
#e.g ./get_ip -h    =    help message
#e.g ./get_ip google.com    =   relays googles IP

import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument('url', help="Input URL without http/s:// e.g google.com", type=str)
args = parser.parse_args()

def url_to_ip():
    print(socket.gethostbyname(args.url))

if url_to_ip() is not None:
    print(url_to_ip())