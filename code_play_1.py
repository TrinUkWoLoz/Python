#!/usr/bin/python3

#variable, floating point, user input for income value
income = float(input("Enter the annual income: "))

#if income is less than stated amount then
if income < 85528.2:
    #0.18 * 80,000 - 556.2 = 13843.8 (Division, multiplication, subtraction)
    tax = 18/100 * income - 556.2
else:
    # income (90000) % 85528 (modulus can only take integers) = 4472
    # 4472 * 0.32 = 1431.04
    # 14839.2 - 1431.04 = 16270.24000000002
    tax = 14839.2 + income % 85528 * 32/100

#rounds to 1dp
tax = round(tax, 0)
print("The tax is:", tax, "thalers")


#Priority	   Operator
#1	           +, -	            unary
#2	           **
#3	           *, /, //, %

#4	           +, -	            binary
#5	           <, <=, >, >=
#6	           ==, !=






