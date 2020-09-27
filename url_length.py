#!/usr/bin/python3.8

import urllib

from urllib.request import urlopen

url = 'http://docs.python.org/lib/module-urllib.html'
url_file = urlopen(url)
urllib_docs = url_file.read()
url_file.close()