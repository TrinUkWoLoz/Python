# List example

# Number of elements provided by user input and stored in num var.
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

# For every element in range - element values provided by user input and stored in val var.
for i in range(num):
    val = float(input("Enter a list element: "))
    myList.append(val)

# If i in list value is greater than, value of next element then (swapped is True) swap elements
while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]
# All elements swapped value is true so print etc..
print("\nSorted:")
print(myList)
