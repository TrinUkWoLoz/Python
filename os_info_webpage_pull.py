#!/usr/bin/python3

import sys, os, urllib.request
def main():
    print("This is Python Version : {}.{}.{}".format(*sys.version_info))
    # os module
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    # urllib module
    page = urllib.request.urlopen('http://google.com/')
    for line in page:
        print(str(line, encoding='utf-8'), end='')
if __name__ == "__main__":
    main()

