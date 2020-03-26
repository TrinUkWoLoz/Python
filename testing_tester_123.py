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

# x = 4
# y = 1
#
# a = x & y         #  = 0    (calculate binary values and follow comparison rule 1+1 =1 and anything else =0)
# b = x | y         #  = 5
# c = ~x            #  = -5   (unary complement (flips binary 1s to 0s and 0s to 1s))
# d = x ^ 5         #  = 1
# e = x >> 2        #  = 1    (calculate binary value, shift right (2 places) and convert to integer)
# f = x << 2        #  = 16   (162**2=4 4*4)
#
# print(a, b, c, d, e, f)

#Next example
# x = 1
# y = 0
#
# z = ((x == y) and (x == y)) or not(x == y)
# print(not(z))

#z = False
#
# hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
#
# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.
#
# # Step 2: write a line of code here that removes the last element from the list.
#
# # Step 3: write a line of code here that prints the length of the existing list.
#
# print("This is the original list:", hatList)
#
# user_input = input("Please enter an integer to replace the middle number in the list:")
# hatList[2] = user_input
#
# print("Result after swapping middle element for user input", hatList)
#
# del hatList[4]
#
# print("Result after 5th element removal", hatList)
#
# print("Number of elements:", (len(hatList)))

# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)
#
# ###
#
# numbers.append(4)
#
# print(len(numbers))
# print(numbers)

###

# myList = []        # creating an empty list
#
# for i in range(5):
#     myList.append(i + 1)
#
# print(myList)
#
# myList = [10, 1, 8, 3, 5]
# total = 0
#
# for i in myList:
#     total += i
#
# print("The total of the values in the list is:", total)
#




# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following members of the band to the list:
# John Lennon, Paul McCartney, and George Harrison;

# step 3: use the for loop and the append() method to prompt the user to add the following
# members of the band to the list: Stu Sutcliffe, and Pete Best;

# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

# I use for loop for append for more convenience
# step 1
#
# beatles=[]
# startlist=["John Lennon","Paul McCartney","George Harrison"]
# templist=["Stu Sutcliffe","Pete Best"]
# print("Step 1:", beatles)
# # step 2
# for i in startlist:
# beatles.append(i)
# print("Step 2:", beatles)
# # step 3
# for i in templist:
# beatles.append(i)
# print("Step 3:", beatles)
# # step 4
# for i in range(2):
# del beatles[-1]
# print("Step 4:", beatles)
# # step 5
# beatles.insert(0,"Ringo Starr")
# print("Step 5:", beatles)
# # testing list legth
# print("The Fab", len(beatles))

#
# myList = []
# swapped = True
# num = int(input("How many elements do you want to sort: "))
#
# for i in range(num):
#     val = float(input("Enter a list element: "))
#     myList.append(val)
#
# while swapped:
#     swapped = False
#     for i in range(len(myList) - 1):
#         if myList[i] > myList[i + 1]:
#             swapped = True
#             myList[i], myList[i + 1] = myList[i + 1], myList[i]
#
# print("\nSorted:")
# print(myList)

# list1 = [1]
# list2 = list1
# list1[0] = 2
# print(list2)

#use my script:
myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist=[]
for i in range(0,len(myList)):
    if myList[i] not in newlist:
    newlist.append(myList[i])
print("The list with unique elements only:")
print(newlist)