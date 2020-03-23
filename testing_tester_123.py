#!/usr/bin/python3.7

# n = 3
#
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

# while n is greater than 0 do
#     print 3+1 = 4
#     n = 4-1 = 2
#     print 2+1 = 3
#     n = 4-1 = 1
#     print 1+1 = 2
#     n = 4-1 = 0
#     else:
#     print 0

#Minus 1 each time | starting at 0 | ending at 4
# n = range(4)
#
# for num in n:
#     print(num - 1)
# else:
#     print(num)

#0-5 range | increments of 3 | prints just 0 and 3
# for i in range(0, 6, 3):
#     print(i)

# var = 17
# varRight = var >> 1
# varLeft = var << 2
# print(var, varLeft, varRight)

x = 4
y = 1

a = x & y         #  = disjunction, of 4 and 2 = False
b = x | y         #  = disjunction, of 4 or 2 = True
c = ~x            #  = negation, 4 and 2 - falsified = False
d = x ^ 5         #  = to the power of (4**5) = 1024
e = x >> 2        #  = 4//2=2 2**2           = 4
f = x << 2        #  = 2**2=4 4*4            = 16

print(a, b, c, d, e, f)


