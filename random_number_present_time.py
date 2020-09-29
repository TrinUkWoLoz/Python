#!/usr/bin/python3
import sys, os, urllib.request, random, datetime
def main():
    print("This is Python Version : {}.{}.{}".format(*sys.version_info))
    # random module
    print(random.randint(1, 1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    random.shuffle(x)
    print(x)
    PresentTime = datetime.datetime.now()
    print(PresentTime)
    print(PresentTime.year, PresentTime.month, PresentTime.day, PresentTime.hour, PresentTime.minute, PresentTime.second, PresentTime.microsecond)
if __name__ == "__main__":
    main()