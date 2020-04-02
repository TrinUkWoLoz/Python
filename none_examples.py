

# Example 1
# If value = none is true then print string
value = None
if value == None:
   print("Sorry, you don't carry any value")



# Example 2
def strangeFunction(n):
    if (n % 2 == 0):
        return True
print(strangeFunction(2))
print(strangeFunction(1))
# Result:
# True
# None



# Example 3
def sumOfList(lst):
    sum = 0

    for elem in lst:
        sum += elem

    return sum

print(sumOfList([5, 4, 3]))


# Example 4
def strangeListFunction(n):
    strangeList = []

    for i in range(0, n):
        strangeList.insert(0, i)

    return strangeList

print(strangeListFunction(5))
# Returns [4, 3, 2, 1, 0]
