#!/usr/bin/python3
import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument('url', help="Check a url for straight quotes", type=str)
args = parser.parse_args()
#print(args.url)

def url_to_ip():
    print(socket.gethostbyname(args.url))

if url_to_ip() is not None:
    print(url_to_ip())







