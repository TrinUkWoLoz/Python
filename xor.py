# ^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary

x = 20
y = 4

result = x ^ y
print("20 ^ 4 =", result)

#Convert integers to binary
#   00010100    =     20
#   00000100    =      4
#   00010000    =    Result(Integer 16)

#Matching inputs of 1+0=1 and 0+1=1 result in 1
#However 0+0 and 1+1 do not equal 1

# Input1      Input2      Output
#  0            0           0
#  0            1           1
#  1            0           1
#  1            1           0