# & does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary

#Bitwise ampersand (&) operator example
x = 4
y = 1
a = x & y
print("a =", a)

#Figure out binary values for the integers
# 4/2= 2+0
# 2/2= 1+0
# 1/2= 0+1        = 0100

# 1/2= 0+1
# 0/2= 0+0        = 0001

#Compare the two binary values and use below rule
# 1+1=1 | 0+1=0 | 1+0=0 | 0+0=0
#    0100
#    0001
#    0000    =   0