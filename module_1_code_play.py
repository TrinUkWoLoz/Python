#!/usr/bin/python3

print()
print("Hello this is wizard the badman")
print("This is the start of my code play")
print("The itsy bitsy spider", "climbed up", "the waterspout.")

print()
print("Assigning variable")
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

print()
print("Assigning variable")
var = "3.7.1"
print("Python version: " + var)

print()
print("Basic calcs with variables")
john = 3
mary = 5
adam = 6
print(john , mary , adam)
totalApples = john + mary + adam
print(totalApples)

print()
print("input function example, prompts user for input")
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

print("\nFloat allowing input of integer")
anything = float(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)

print("\nNew line within string and concatenation - operator within string")
fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")

print("\nReplication by using * within string")
print("James" * 3)

print("\nRectangle example")
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

print("\nConvert a number into a string using str() function")
leg_a = float(input("Input first leg length: "))
leg_b = float(input("Input second leg length: "))
print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

print("\nSimple maths test")
# input a float value for variable a here
a_is_for_awesome = float(input("Insert variable a now:"))
# input a float value for variable b here
b_is_for_brave = float(input("Insert variable a now:"))
# output the result of addition here
print(a_is_for_awesome + b_is_for_brave)
# output the result of subtraction here
print(a_is_for_awesome - b_is_for_brave)
# output the result of multiplication here
print(a_is_for_awesome * b_is_for_brave)
# output the result of division here
print(a_is_for_awesome / b_is_for_brave)
print("\nThat's all, folks!")






