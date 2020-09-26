#!/usr/bin/python3.8

import os

#Change directory and create directory called test
os.chdir('/home/wizard/Documents')
os.mkdir('test')

f = open("/home/wizard/Documents/test/new_file.txt", "w")   # 'r' for reading and 'w' for writing
f.write("Hello World")    # Write inside file






