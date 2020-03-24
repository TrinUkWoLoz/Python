#Lists examples

hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code here that removes the last element from the list.

# Step 3: write a line of code here that prints the length of the existing list.

print("This is the original list:", hatList)

user_input = input("Please enter an integer to replace the middle number in the list:")
hatList[2] = user_input

print("Result after swapping middle element for user input", hatList)

del hatList[4]

print("Result after 5th element removal", hatList)

print("Number of elements:", (len(hatList)))