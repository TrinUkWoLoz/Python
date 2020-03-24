numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

#Glue on value 4 as the last element
numbers.append(4)
print(len(numbers))
print("Value 4 added as the last element:")
print(numbers)
print()

myList = []        # creating an empty list

for i in range(5):
    myList.append(i + 1)

print("This is a list with a for loop, range and append:", myList)