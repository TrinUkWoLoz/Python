#!/usr/bin/python3.7
# The pyramid is stacked according to one simple principle: each lower layer contains one block more than the layer above.
# Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.
# Note: the height is measured by the number of fully completed layers - if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.


# blocks = int(input("Enter the number of blocks: "))
# height = 0
# while blocks > 0:
#     height += 1
#     blocks = blocks - (height +1)
#
# print("The height of the pyramid:", height)

#First loop
#blocks = 6
#height = 0
#blocks is greater than 0
#height = height + 1 | height = 0 + 1 | height = 1
#blocks = 6 - (1+1) | blocks = 4

#Second loop
#Height = 1+1=2
#Blocks = 4-(2+1)

#Third loop
#Height = 2+1=3
#Blocks = 1-(3+1)=-3

#Then exits loop because blocks is < 0


