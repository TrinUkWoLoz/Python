# List slice examples

# Outcome is '1' because list1's contents were copied to list2 (:)
# then 1st (0) element of list1 was assigned '2' and list2 printed
list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list2)

# A slice of this form makes a new (target) list, taking elements from
# the source list - the elements of the indices from start to end - 1.
# Note: not to end but to end - 1. An element with an index equal to end
# is the first element which does not take part in the slicing.
# The newList list will have end - start (3 - 1 = 2) elements -
# the ones with indices equal to 1 and 2 (but not 3).
# The snippet's output is: [8, 6]

myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

# So '8' (element 1) is the index of the first element included in the slice
# and '2' (element -1) is the first element not included in the slice
#Element: 0   1  2  3 -1
myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]
print(newList)

# Start is 3rd element (4) - last element is sum of values in list (last value 2) 4th element
myList = [10, 8, 6, 4, 2]
newList = myList[3:]
print(newList)

# The previously described del instruction is able to delete more than
# just a list's element at once - it can delete slices too:
# Deleting slice example
myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

