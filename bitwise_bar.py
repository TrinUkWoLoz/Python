# | does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary

x = 20
y = 4

result = x|y
print("20 | 4 =", result)

#Convert integers to binary
#   00010100    =     20
#   00000100    =      4
#   00010100    =    Result(Integer 20)

#Matching inputs of 1 result in 1 also 1+0=1 like 0+1=1
#However 0+0 does not

# Input1      Input2      Output
#  0            0           0
#  0            1           1
#  1            0           1
#  1            1           1
