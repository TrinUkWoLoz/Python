#!/usr/bin/python3.7

import os

shutdown = input("Sir Wizard, would you like to shutdown your device(yes/no): ")
if shutdown == 'no':
    exit()
else:
#    os.system("shutdown /s /t 1")
    os.system("shutdown -h now")

