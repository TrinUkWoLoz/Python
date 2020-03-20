#!/usr/bin/python3.7

#Range from 2-10 therefore 111 not in range so first print not run
#Second print is run as first isn't (else)
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)
