#!/usr/bin/python3.7

secret_number = 777

print(
"""
+==========================================+
| Welcome to my game, potential muggle!    |
| Enter an integer number                  |
| and guess what magic number I've         |
| picked for you.                          |
| So, what is the magic number?            |
+==========================================+
""")

input_num = int(input("Guess a number to see if your magic: "))

while input_num != secret_number:
    print("Haha your stuck in my infinite loop you muggle chimp")
if input_num == secret_number:
    print("Well done Harry Potter! You are free now. Welcome to Hogwarts.")


