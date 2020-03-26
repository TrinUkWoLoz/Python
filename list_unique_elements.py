# List unique elements only
# For i in full range

myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
newlist=[]
for i in range(0,len(myList)):
    if myList[i] not in newlist:
    newlist.append(myList[i])
print("The list with unique elements only:")
print(newlist)