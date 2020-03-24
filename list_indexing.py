# LIST INDEXING
#
# the list is assigned a sequence of five integer values;
# the i variable takes the values 0, 1, 2, 3, and 4, and then it indexes the list,
# selecting the subsequent elements: the first, second, third, fourth and fifth;
# each of these elements is added together by the += operator to the total variable,
# giving the final result at the end of the loop;
# note the way in which the len() function has been employed - it makes the code
# independent of any possible changes in the list's content.

myList = [10, 1, 8, 3, 5]
total = 0

for i in range(len(myList)):
    total += myList[i]

print("The total of the values in the list is:", total)

# a more efficient way of writing the code would be:

myList = [10, 1, 8, 3, 5]
total = 0

for i in myList:
    total += i

print("\nThis is a more efficient way of writing the code (sum of list values):", total) 



