print("\nThis is a basic variable swap:")

variable1 = 1
variable2 = 2

print("\nOriginal variable1 =", variable1)
print("Original variable2 =", variable2)

variable1, variable2 = variable2, variable1

print("\nThis is now variable1 =", variable1)
print("This is now variable2 =", variable2)

print("\nReversing list using swap and element:")

#Reverse list order by making 2 swaps
myList = [10, 1, 8, 3, 5]
print("\nCurrent list:", myList)

myList[0], myList[4] = myList[4], myList[0]
myList[1], myList[3] = myList[3], myList[1]

print("Reversed list:", myList)
