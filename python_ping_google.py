#!/usr/bin/python

#  Pinging servers in Python
#  
#  If you don't need to support Windows, here's a really concise way to
#  do it:

import os
hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'is up!'
else:
  print hostname, 'is down!'

#  This works because ping returns a non-zero value if the connection
#  fails. (The return value actually differs depending on the network
#  error.) You could also change the ping timeout (in seconds) using the
#  '-t' option.  Note, this will output text to the console.
#  
#  [10flow] [so/q/2953462] [cc by-sa 3.0]
