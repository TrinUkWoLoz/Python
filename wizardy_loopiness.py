#!/usr/bin/python3.7

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

input_num = int(input("Guess a number you muggle chimp: "))

while input_num != secret_number:
    print("Haha your stuck in my infinite loop Harry Potter (Dumbass)")
if input_num == secret_number:
    print("Well done, muggle! You are free now.")


