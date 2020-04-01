#My Python Notes#

#Created by Guido van Rossum (Dutch programmer)

#Open source

#Then developed continuosly by community

#Additions Cython (C python) Rython (Reduced - subset of python for self development) & Jython (Java python)

#Interpreter language such as Java Perl

#Compiler language C & Go (good for fast mathemeatical calculations)

#Function(print), parenthares(()), quotations (intiate string), closing of both ("))
#All but the function make up the 'function invocation'
#All but the function and the parenthares make up the 'argument'
print("Hello this is christopher")

#Within a string \n indicates a new output line
#E.g:       print("Hello\nfriend.")
Displays:   Hello
            friend.
#Seperate multiple arguments like so (They are printed individually with no commas displayed):
print("The itsy bitsy spider" , "climbed up" , "the waterspout.")

#Keyword argument - 'end' is keyword and requires =
#Below code prints: My name is Python. Monty Python.
print("My name is", "Python.", end=" ")
print("Monty Python.")

##########################

#1. The print() function is a built-in function. It prints/outputs a specified message to the screen/consol window.

#2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported. Python 3.7.1 comes with 69 built-in functions. You can find their full list provided in alphabetical order in the Python Standard Library.

#3. To call a function (function invocation), you need to use the function name followed by parentheses. You can pass arguments into a function by placing them inside the parentheses. You must separate arguments with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.

#4. Python strings are delimited with quotes, e.g., "I am a string", or 'I am a string, too'.

#5. Computer programs are collections of instructions. An instruction is a command to perform a specific task when executed, e.g., to print a certain message to the screen.

#6. In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.

#7. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputted after the second, etc.

#8. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.

#9. The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies the separator between the outputted arguments (e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter specifies what to print at the end of the print statement.

#########################


doc2pdf LJCH_CV.docx

#COLOUR LIST#
pink/red = operator
light blue = function
purple = integer/value
grey = comments
green = unrecognised
orange/yellow = string

##########################

#OPERATORS#

#Can simplify by adding op to left side of operator (augmented assignment)
variable = variable op expression
x = x * 2

variable op= expression
x *= 2

#Both the below mean the same
x += 2
x = x + 2


############################

#1. A variable is a named location reserved to store values in the memory. A variable is created or initialized automatically when you assign a value to it for the first time. (2.1.4.1)

#2. Each variable must have a unique name - an identifier. A legal identifier name must be a non-empty sequence of characters, must begin with the underscore(_), or a letter, and it cannot be a Python keyword. The first character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive. (2.1.4.1)

#3. Python is a dynamically-typed language, which means you don't need to declare variables in it. (2.1.4.3) To assign values to variables, you can use a simple assignment operator in the form of the equal (=) sign, i.e., var = 1.

#4. You can also use compound assignment operators (shortcut operators) to modify values assigned to variables, e.g., var += 1, or var /= 5 * 2. (2.1.4.8)

#5. You can assign new values to already existing variables using the assignment operator or one of the compound operators, e.g.: (2.1.4.5)

var = 2
print(var)

var = 3
print(var)

var += 1
print(var)

#6. You can combine text and variables using the + operator, and use the print() function to output strings and variables, e.g.: (2.1.4.4)

var = "007"
print("Agent " + var)

##############################

#Key takeaways

#1. Comments can be used to leave additional information in code. They are omitted at runtime. The information left in source code is addressed to human readers. In Python, a comment is a piece of text that begins with #. The comment extends to the end of line.

#2. If you want to place a comment that spans several lines, you need to place # in front of them all. Moreover, you can use a comment to mark a piece of code that is not needed at the moment (see the last line of the snippet below), e.g.:

# This program prints
# an introduction to the screen.
print("Hello!")  # Invoking the print() function
# print("I'm Python.")

#3. Whenever possible and justified, you should give self-commenting names to variables, e.g., if you're using two variables to store a length and width of something, the variable names length and width may be a better choice than myvar1 and myvar2.

#4. It's important to use comments to make programs easier to understand, and to use readable and meaningful variable names in code. However, it's equally important not to use variable names that are confusing, or leave comments that contain wrong or incorrect information!
#5. Comments can be important when you are reading your own code after some time (trust us, developers do forget what their own code does), and when others are reading your code (can help them understand what your programs do and how they do it more quickly).

########################

#INTEGER FUNCTION#
the int() function takes one argument (e.g., a string: int(string)) and tries to convert it into an integer;
if it fails, the whole program will fail too (there is a workaround for this situation, but we'll show you this a little later);

#FLOAT FUNCTION#
#the float() function takes one argument (e.g., a string: float(string))and tries to convert it into a float (the rest is the same).

#########################

#Key takeaways

#1. The print() function sends data to the console, while the input() function gets data from the console.

#2. The input() function comes with an optional parameter: the prompt string. It allows you to write a message before the user input, e.g.:

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

#3. When the input() function is called, the program's flow is stopped, the prompt symbol keeps blinking (it prompts the user to take action when the console is switched to input mode) until the user has entered an input and/or pressed the Enter key.

#NOTE

#You can test the functionality of the input() function in its full scope locally on your machine. For resource optimization reasons, we have limited the maximum program execution time in Edube to a few seconds. Go to Sandbox, copy-paste the above snippet, run the program, and do nothing - just wait a few seconds to see what happens. Your program should be stopped automatically after a short moment. Now open IDLE, and run the same program there - can you see the difference?

#Tip: the above-mentioned feature of the input() function can be used to prompt the user to end a program. Look at the code below:

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

#3. The result of the input() function is a string. You can add strings to each other using the concatenation (+) operator. Check out this code:

num1 = input("Enter the first number: ") # Enter 12
num2 = input("Enter the second number: ") # Enter 21

print(num1 + num2) # the program returns 1221

#4. You can also multiply (* - replication) strings, e.g.:

myInput = ("Enter something: ") # Example input: hello
print(myInput * 3) # Expected output: hellohellohello


######
#   OPERATORS
######

#MODULUS %
#Divide and check remainder dp

6%2

#Divide left by right
6/2 = 3
#evaluates to 0 as there is no remainder

7%2

7/2=3.5
#evaluates to 1 as there is 1dp remainder

11 % 4
11 / 4 = 2
2 * 4 = 8
11 - 8 = 3

4 % 3
1


#Exponentiation **
#Square

6**2
6*6= 36

6**3
6*6 = 36*6 = 216

#Floor Division //
#Rounds to the next smaller integer or float with .0 as decimal point

5/2 = 2.5
5//2 = 2

5.0/2 = 2.5
5.0//2 = 2.0

##########################

#         MODULE 3

###########################

#OPERATORS

# = is an assignment operator, e.g., a = b assigns a with the value of b;

# == is the question are these values equal?; a == b compares a and b

# It is a binary operator with left-sided binding. It needs two arguments and checks if they are equal


#Priority	   Operator         (3 done first, 1 last)

#1	           +, -	            unary
#2	           **
#3	           *, /, //, %

#4	           +, -	            binary
#5	           <, <=, >, >=
#6	           ==, !=

#Abreviation - using operators to print True/False result based on input and calc rule

#Using one of the comparison operators in Python,
#write a simple two-line program that takes the parameter n as input,
#which is an integer, and prints False if n is less than 100,
#and True if n is greater than or equal to 100

n = int(input("Enter your number: "))
print(n>=100)

#if statement

if true_or_not:
    do_this_if_true

T#his conditional statement consists of the following, strictly necessary, elements in this and this order only:

#the if keyword;
#one or more white spaces;
#an expression (a question or an answer) whose value will be interpreted solely in terms of True (when its value is non-zero) and False (when it is equal to zero);
#a colon followed by a newline;
#an indented instruction or set of instructions (at least one instruction is absolutely required);
#the indentation may be achieved in two ways - by inserting a particular number of spaces (the recommendation is to use four spaces of indentation),
#or by using the tab character; note: if there is more than one instruction in the indented part, the indentation should be the same in all lines;
#even though it may look the same if you use tabs mixed with spaces, it's important to make all indentations exactly the same -
#Python 3 does not allow mixing spaces and tabs for indentation

#if basic structure

if the_weather_is_good:
    go_for_a_walk()
have_lunch()

#if sheep_counter variable greater than or equal to 120 then 3 following functions are carried out
#feed_the_sheepdogs function carried out regardless

if sheep_counter >= 120:
    make_a_bed()
    take_a_shower()
    sleep_and_dream()
feed_the_sheepdogs()

#if else basic structure

if true_or_false_condition:
    perform_if_condition_true
else:
    perform_if_condition_false

#another example
if the_weather_is_good:
    go_for_a_walk()
    have_fun()
else:
    go_to_a_theater()
    enjoy_the_movie()
have_lunch()

#nested if statement
if the_weather_is_good:
    if nice_restaurant_is_found:
        have_lunch()
    else:
        eat_a_sandwich()
else:
    if tickets_are_available:
        go_to_the_theater()
    else:
        go_shopping()

#elif basic structure
if the_weather_is_good
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

#Abreviation example for detect higher number example
# read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# print the result
print("The larger number is:", larger_number)

#Write a program that utilizes the concept of conditional execution, takes a string as input, and:

#prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
#prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

plant = input("Type in a really cool plant: ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")

elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum")

else:
    print("Spathiphyllum, not ", plant)

#Execute if True
x = 10

if x == 10: # condition
    print("x is equal to 10") # executed if the condition is True

#Execute if true or false
x = 10

if x < 10: # condition
    print("x is less than 10") # executed if the condition is True

else:
    print("x is greater than or equal to 10") # executed if the condition is False

#Including elif with both of the above examples
x = 10

if x > 5: # True
    if x == 6: # False
        print("nested: x == 6")
    elif x == 10: # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")

#Example of setting variables twice
x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)

#Check
#False
#True

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

#Check
#True
#False

#Number of rules in play

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")

#Check
#one
#two

#While loop structure
#while repeats the execution as long as the condition evaluates to True.
while conditional_expression:
    instruction

#Infinite loop
while True:
    print("I'm stuck inside a loop.")

#Using a counter variable to exit loop
counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)

#for i loop basic structure
for i in range(100):
    # do_something()
    pass

# the for keyword opens the for loop; note - there's no condition after it; you don't have to think about conditions,
# as they're checked internally, without any intervention;

# any variable after the for keyword is the control variable of the loop; it counts the loop's turns, and does it automatically;

# the in keyword introduces a syntax element describing the range of possible values being assigned to the control variable;

# the range() function (this is a very special function) is responsible for generating all the desired values of the control variable;

# in our example, the function will create (we can even say that it will feed the loop with) subsequent values from the
# following set: 0, 1, 2 .. 97, 98, 99; note: in this case, the range() function starts its job from 0 and finishes
# it one step (one integer number) before the value of its argument;

# note the pass keyword inside the loop body - it does nothing at all; it's an empty instruction - we put it here because the for loop's
# syntax demands at least one instruction inside the body (by the way - if, elif, else and while express the same thing)

#For i loop with 2 arguments - 1st argument = starting # - 2nd argument range end #
for i in range(2, 8):
    print("The value of i is currently", i)

#For i loop with 3 arguments - 1st argument = starting # - 2nd argument range end # - 3rd argument = increments (every 3 - 2,5)
for i in range(2, 8, 3):
    print("The value of i is currently", i)

#break + continue example - input numbers until -1 is entered and then display highest number inputted
largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue            #or break
    counter += 1

    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

#Another loopy example
secretword = "chupacabra"
word = input("Guess secret word: ")

while word != secretword:
    word = input("Guess again: ")
else:
    print("You have sucessfully left the loop.")

#The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
#It can be used with both the while and for loops.

#While, else basic structure
i = 1
while i < 10:
    print(i)
    i += 1
else:
    print("else:", i)

#The range() function generates a sequence of numbers. It accepts integers and returns range objects.
# The syntax of range() looks as follows: range(start, stop, step), where:

#start is an optional parameter specifying the starting number of the sequence (0 by default)
#stop is an optional parameter specifying the end of the sequence generated (it is not included),
#and step is an optional parameter specifying the difference between the numbers in the sequence (1 by default.)

#Range example print odd numbers to screen
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

#While loop print odd numbers to screen
x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

#Break for loop at certain character
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

#For loop that replaces each 0 with x
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

#Logical operators - conjunctions (and) and disjunctions (or)

#And
#is a binary operator with a priority that is lower than the one expressed by the comparison operators
#It allows us to code complex conditions without the use of parentheses
#The result provided by the and operator can be determined on the basis of the truth table.
#   Argument A	Argument B	A and B
#    False	    False	    False
#    False	    True	    False
#    True	    False	    False
#    True	    True	    True

#or
#A disjunction operator is the word or. It's a binary operator with a lower priority than and (just like + compared to *). ' \ ''
#Its truth table is as follows:
#Argument A	Argument B	A or B
#False	    False	    False
#False	    True	    True
#True	    False	    True
#True	    True	    True

#not
#is another operator that can be applied for constructing conditions. ' \ '
#It's a unary operator performing a logical negation. Its operation is simple: it turns truth into falsehood and falsehood into truth
#This operator is written as the word not, and its priority is very high: the same as the unary + and -.
#Truth table:
# Argument      not Argument
# False	            True
# True	            False

#Logical Expressions
#You may be familiar with De Morgan's laws. They say that:
#The negation of a conjunction is the disjunction of the negations.
#The negation of a disjunction is the conjunction of the negations.

#Let's write the same thing using Python:

#not (p and q) == (not p) or (not q)
#not (p or q) == (not p) and (not q)

#Note how the parentheses have been used to code the expressions - we put them there to improve readability.
#We should add that none of these two-argument operators can be used in the abbreviated form known as op=. This exception is worth remembering.

#Logical v single-bits
# Logical operators take their arguments as a whole regardless of how many bits they contain.
# The operators are aware only of the value: zero (when all the bits are reset) means False;
# not zero (when at least one bit is set) means True.
#
# The result of their operations is one of these values: False or True.
# This means that this snippet will assign the value True to the j variable if i is not zero;
# otherwise, it will be False.
#
# i = 1
# j = not not i

#Bitwise Operators
#However, there are four operators that allow you to manipulate single bits of data.
#They are called bitwise operators.

#They cover all the operations we mentioned before in the logical context,
#and one additional operator. This is the xor (as in exclusive or) operator, and is denoted as ^ (caret).

#Here are all of them:

#   & (ampersand)   -     bitwise conjunction;
#   | (bar)         -     bitwise disjunction;
#   ~ (tilde)       -     bitwise negation;
#   ^ (caret)       -     bitwise exclusive or (xor)

#Bitwise operations (ampersand &, bar |, circumflex accent/caret ^)
#   Arg A	Arg B	Arg B & Arg B	Arg A | Arg B	Arg A ^ Arg B
#   0	    0	        0	            0	                0
#   0	    1	        0	            1	                1
#   1	    0	        0	            1	                1
#   1	    1	        1	            1	                0

#Bitwise operations (tilde ~)
#   Arg	    ~Arg
#   0	      1
#   1	      0

#   & requires exactly two 1s to provide 1 as the result;
#   | requires at least one 1 to provide 1 as the result;
#   ^ requires exactly one 1 to provide 1 as the result.

#Shift operators (diagraphs << >>)
#The shift operators in Python are a pair of digraphs: << and >>, clearly suggesting in which direction the shift will act.

#value << bits
#value >> bits

#The left argument of these operators is an integer value whose bits are shifted. The right argument determines the size of the shift.
#It shows that this operation is certainly not commutative

var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)

# This is not explained properly.
# I expect it to mention << as multiplication(*), >> as division(//) and the bits as 2power2 or 2power1
# so that it is easy to understand, like below.

# 17>>1=8     (left to right)
# 17//2=8     8**1=8

# 17<<2=68   (right to left)
# 2**2=4     4*17=68

Priority	Operator
1	        ~, +, -	        unary
2	        **
3	        *, /, //, %

4	        +, -	        binary
5	        <<, >>
6	        <, <=, >, >=
7	        ==, !=
8	        &
9	        |
10	        =, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=

# Key takeaways
#
# 1. Python supports the following logical operators:
#
# and → if both operands are true, the condition is true, e.g., (True and True) is True,
# or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
# not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
# 2. You can use bitwise operators to manipulate single bits of data. The following sample data:
#
# x = 15, which is 0000 1111 in binary,
# y = 16, which is 0001 0000 in binary.
# will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:
#
# & does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
# | does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
# ˜ does a bitwise not, e.g., ˜ x = 240, which is 1111 0000 in binary,
# ^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
# >> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
# << does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,

#Convert an integer to binary
# 12:2  =  6+0
# 6:2   =  3+0
# 3:2   =  1+1
# 1:2   =  0+1

# Here is an example of such conversion using the integer 12.
# First, let’s divide the number by two specifying quotient and remainder:
# Now, we simply need to write out the remainder in the reverse order —1100.
# So, 12 in decimal system is represented as 1100 in binary.

#Bitwise & operator example
# x = 4
# y = 1
# a = x & y

#Figure out binary values for the integers
# 4/2= 2+0
# 2/2= 1+0
# 1/2= 0+1        = 0100

# 1/2= 0+1
# 0/2= 0+0        = 0001

#Compare the two binary values
# 1+1=1 | 0+1=0 | 1+0=0 | 0+0=0
#    0100
#    0001
#    0000    =   0

#Bitwise >> (right shift) operator example
# x = 4
# y = 1
# e = x >> 2

# x (value) >> n (number of shifts)

# 0100 (shift two places to the right)
# 0001  = 1  (0001 is binary for 1)

#Bitwise >> (left shift) operator example
# x = 4
# y = 1
# e = x << 2

# x (value) << n (number of shifts)

# 0100 (shift two places to the left)
# 10000  = 16  (10000 is binary for 16)

#Python binary to decimal converting functions (bin | int)

#Convert integer 4 to binary
#   >> bin(4)
#   >> '0b100'          (=0100)

#Convert binary 0100 to integer
#   >> int(0b100)       (0b100 = 0100)
#   >> 4

#Bitwise complement (~)
# x = 4
# c = ~x
# General rule: c = -x-1
# c = -4-1
# c = -5

#Bitwise ^ (xor)
# x = 4
# d = x ^ 5

#Bitwise | (bar)
# x = 4
# y = 1
# b = x | y
# Covert both values to binary (4=0100 1=0001)

#Integer conversion to binary (example =20 | 16+4=20 so.....)
128 64 32 16 8 4 2 1  =  2**7 2**6 2**5 **4 2**3 2**2 2**1 2**0
 0   0  0  1 0 1 0 0  =  20 (integer value)

# Key takeaways
#
# 1. Python supports the following logical operators:
#
# and → if both operands are true, the condition is true, e.g., (True and True) is True,
# or → if any of the operands are true, the condition is true, e.g., (True or False) is True,
# not → returns false if the result is true, and returns true if the result is false, e.g., not True is False.
# 2. You can use bitwise operators to manipulate single bits of data. The following sample data:
#
# x = 15, which is 0000 1111 in binary,
# y = 16, which is 0001 0000 in binary.
# will be used to illustrate the meaning of bitwise operators in Python. Analyze the examples below:
#
# & does a bitwise and, e.g., x & y = 0, which is 0000 0000 in binary,
# | does a bitwise or, e.g., x | y = 31, which is 0001 1111 in binary,
# ˜ does a bitwise not, e.g., ˜ x = 240, which is 1111 0000 in binary,
# ^ does a bitwise xor, e.g., x ^ y = 31, which is 0001 1111 in binary,
# >> does a bitwise right shift, e.g., y >> 1 = 8, which is 0000 1000 in binary,
# << does a bitwise left shift, e.g., y << 3 = , which is 1000 0000 in binary,

#################################

#LISTS#

##################################

# List is a collection of elements, but each element is a scalar
# So far, you've learned how to declare variables that are able to store exactly one given value at a time. ' \
# Such variables are sometimes called scalars by analogy with mathematics.
#
# Multi value variables
#
# numbers = [10, 5, 7, 2, 1]
#
# Let's say the same thing using adequate terminology: numbers is a list consisting of five values, all of them numbers.
# We can also say that this statement creates a list of length equal to five (as in there are five elements inside it).
#
# The elements inside a list may have different types. Some of them may be integers, others floats, and yet others may be lists.
#
# Python has adopted a convention stating that the elements in a list are always numbered starting from zero.
# This means that the item stored at the beginning of the list will have the number zero.
# Since there are five elements in our list, the last of them is assigned the number four. Don't forget this.

#Assigns 5 integers to var numbers
numbers = [10, 5, 7, 2, 1]
print("List content:", numbers) # printing original list content

#Amends first integer from 10 to 111
numbers[0] = 111
print("New list content: ", numbers) # current list content

#Copies element 5 (numbers[4]) to element 2 (numbers[1])
numbers[1] = numbers[4] # copying value of the fifth element to the second
print("New list content:", numbers) # printing current list content

# The value inside the brackets which selects one element of the list is called an index, while the operation
# of selecting an element from the list is known as indexing.

# The len() function
# The length of a list may vary during execution. New elements may be added to the list, while others may be removed from it.
# This means that the list is a very dynamic entity.
#
# If you want to check the list's current length, you can use a function named len() (its name comes from length).
#
# The function takes the list's name as an argument, and returns the number of elements currently stored inside the list
# in other words the list's length

print("\nList length:", len(numbers)) # printing the list's length

# Removing elements from a list
# Any of the list's elements may be removed at any time - this is done with an instruction named del (delete). ' \
#                'Note: it's an instruction, not a function.
#
# You have to point to the element to be removed - it'll vanish from the list, and the list's length will be reduced by one.
#
# Look at the snippet below. Can you guess what output it will produce? Run the program in the editor and check.

del numbers[1]
print(len(numbers))
print(numbers)

# Negative indices are legal
# It may look strange, but negative indices are legal, and can be very useful.
#
# An element with an index equal to -1 is the last one in the list.

print(numbers[-1])

# The example snippet will output 1. Run the program and check.
# Similarly, the element with an index equal to -2 is the one before last in the list.

print(numbers[-2])

# The example snippet will output 2.
#
# The last accessible element in our list is numbers[-4] (the first one) - don't try to go any further!

# Functions vs. methods
# A method is a specific kind of function - it behaves like a function and looks like a function, but differs in the way in which it acts, and in its invocation style.
#
# A function doesn't belong to any data - it gets data, it may create new data and it (generally) produces a result.
#
# A method does all these things, but is also able to change the state of a selected entity.
#
# A method is owned by the data it works for, while a function is owned by the whole code.
#
#
# This also means that invoking a method requires some specification of the data from which the method is invoked.
#
# It may sound puzzling here, but we'll deal with it in depth when we delve into object-oriented programming.
#
# In general, a typical function invocation may look like this:
#

result = function(arg)

# A typical method invocation usually looks like this:

result = data.method(arg)

# Note: the name of the method is preceded by the name of the data which owns the method.
# Next, you add a dot, followed by the method name, and a pair of parenthesis enclosing the arguments.
#
# The method will behave like a function, but can do something more - it can change the internal state of the data
# from which it has been invoked

# Adding elements to a list: continued
# You can start a list's life by making it empty (this is done with an empty pair of square brackets)
# and then adding new elements to it as needed.

# Key takeaways
#
# 1. The list is a type of data in Python used to store multiple objects.
# It is an ordered and mutable collection of comma-separated items between square brackets, e.g.:

myList = [1, None, True, "I am a string", 256, 0]

# 2. Lists can be indexed and updated, e.g.:

myList = [1, None, True, 'I am a string', 256, 0]
print(myList[3]) # outputs: I am a string
print(myList[-1]) # outputs: 0

myList[1] = '?'
print(myList) # outputs: [1, '?', True, 'I am a string', 256, 0]

myList.insert(0, "first")
myList.append("last")
print(myList) # outputs: ['first', 1, '?', True, 'I am a string', 256, 0, 'last']

# 3. Lists can be nested, e.g.: myList = [1, 'a', ["list", 64, [0, 1], False]].
#
# You will learn more about nesting in module 3.1.7 - for the time being,
# we just want you to be aware that something like this is possible, too.
#
# 4. List elements and lists can be deleted, e.g.:

myList = [1, 2, 3, 4]
del myList[2]
print(myList) # outputs: [1, 2, 4]

del myList # deletes the whole list

# Again, you will learn more about this in module 3.1.6 - don't worry. ' \
# For the time being just try to experiment with the above code and check how changing it affects the output.
#
# 5. Lists can be iterated through using the for loop, e.g.:

myList = ["white", "purple", "blue", "yellow", "green"]

for color in myList:
    print(color)

# 6. The len() function may be used to check the list's length, e.g.:

myList = ["white", "purple", "blue", "yellow", "green"]
print(len(myList)) # outputs 5

del myList[2]
print(len(myList)) # outputs 4

# 7. A typical function invocation looks as follows:
    result = function(arg)
# while a typical method invocation looks like this:
    result = data.method(arg)


# Key takeaways
#
# 1. You can use the sort() method to sort elements of a list, e.g.:

lst = [5, 3, 1, 2, 4]
print(lst)

lst.sort()
print(lst) # outputs: [1, 2, 3, 4, 5]

# 2. There is also a list method called reverse(), which you can use to reverse the list, e.g.:

lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst) # outputs: [4, 2, 1, 3, 5]


# the name of an ordinary variable is the name of its content;
# the name of a list is the name of a memory location where the list is stored.
# Read these two lines once more - the difference is essential for understanding what we are going to talk about next.
#
# The assignment: list2 = list1 copies the name of the array, not its contents. In effect, the two names
# (list1 and list2) identify the same location in the computer memory. Modifying one of them affects the other,
# and vice versa.


# Powerful slices
# Fortunately, the solution is at your fingertips - its name is the slice.
#
# A slice is an element of Python syntax that allows you to make a brand new copy of a list, or parts of a list.
#
# It actually copies the list's contents, not the list's name.

# One of the most general forms of the slice looks as follows:
#
# myList[start:end]
#
# As you can see, it resembles indexing, but the colon inside makes a big difference.
#
# A slice of this form makes a new (target) list, taking elements from the source list -
# the elements of the indices from start to end - 1.
#
# Note: not to end but to end - 1. An element with an index equal to end is the first element
# which does not take part in the slicing.
#
# Using negative values for both start and end is possible (just like in indexing).
#
# Take a look at the snippet:

myList = [10, 8, 6, 4, 2]
newList = myList[1:3]
print(newList)

# The newList list will have end - start (3 - 1 = 2) elements - the ones with indices equal to 1 and 2 (but not 3).
#
# The snippet's output is: [8, 6]

# start is the index of the first element included in the slice;
# end is the index of the first element not included in the slice.
# myList[start:end]

# So '8' (element 1) is the index of the first element included in the slice
# and '2' (element -1) is the first element not included in the slice
# start=1

#Element: 0   1  2  3 -1
myList = [10, 8, 6, 4, 2]
newList = myList[1:-1]
print(newList)

# Slices: continued
# If you omit the start in your slice, it is assumed that you want to get a slice beginning at the element with index 0.
# In other words, the slice of this form:

myList[:end]

# or

myList[0:end]

# Similarly, if you omit the end in your slice, it is assumed that you want the slice to
# end at the element with the index len(myList).
# In other words, the slice of this form:

myList[start:]

# is a more compact equivalent of:

myList[start:len(myList)]

# The in and not in operators
# Python offers two very powerful operators, able to look through the
# list in order to check whether a specific value is stored inside the list or not.
# These operators are:

elem in myList
elem not in myList

# The first of them (in) checks if a given element (its left argument) is currently
# stored somewhere inside the list (the right argument) - the operator returns True in this case.
#
# The second (not in) checks if a given element (its left argument) is absent in a
# list - the operator returns True in this case.

# Key takeaways
#
# 1. If you have a list l1, then the following assignment:
# l2 = l1 does not make a copy of the l1 list, but makes the variables l1
# and l2 point to one and the same list in memory. For example:

vehiclesOne = ['car', 'bicycle', 'motor']
print(vehiclesOne) # outputs: ['car', 'bicycle', 'motor']

vehiclesTwo = vehiclesOne
del vehiclesOne[0] # deletes 'car'
print(vehiclesTwo) # outputs: ['bicycle', 'motor']

# 2. If you want to copy a list or part of the list, you can do it by performing slicing:

colors = ['red', 'green', 'orange']

copyWholeColors = colors[:] # copy the whole list
copyPartColors = colors[0:2] # copy part of the list

# 3. You can use negative indices to perform slices, too. For example:

sampleList = ["A", "B", "C", "D", "E"]
newList = sampleList[2:-1]
print(newList) # outputs: ['C', 'D']

# 4. The start and end parameters are optional when performing a slice: list[start:end], e.g.:

myList = [1, 2, 3, 4, 5]
sliceOne = myList[2: ]
sliceTwo = myList[ :2]
sliceThree = myList[-2: ]

print(sliceOne) # outputs: [3, 4, 5]
print(sliceTwo) # outputs: [1, 2]
print(sliceThree) # outputs: [4, 5]

# 5. You can delete slices using the del instruction:

myList = [1, 2, 3, 4, 5]
del myList[0:2]
print(myList) # outputs: [3, 4, 5]

del myList[:]
print(myList) # deletes the list content, outputs: []

# 6. You can test if some items exist in a list or not using the keywords in and not in, e.g.:

myList = ["A", "B", 1, 2]

print("A" in myList) # outputs: True
print("C" not in myList) # outputs: True
print(2 not in myList) # outputs: False


# Lists in lists
# Lists can consist of scalars (namely numbers) and
# elements of a much more complex structure (you've already
# seen such examples as strings, booleans, or even other lists in
# the previous Section Summary lessons). Let's have a closer look at
# the case where a list's elements are just lists.
# We often find such arrays in our lives. Probably the best example of this is a chessboard.

row = [WHITE_PAWN for i in range(8)]

# The part of the code placed inside the brackets specifies:
#
# the data to be used to fill the list (WHITE_PAWN)
# the clause specifying how many times the data occurs inside the list (for i in range(8))
# Let us show you some other list comprehension examples:
#
# Example #1:

squares = [x ** 2 for x in range(10)]

# The snippet produces a ten-element list filled with squares of ten integer numbers
# starting from zero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
#
# Example #2:

twos = [2 ** i for i in range(8)]

# The snippet creates an eight-element array containing the first eight powers of two (1, 2, 4, 8, 16, 32, 64, 128)
#
# Example #3:

odds = [x for x in squares if x % 2 != 0 ]

# The snippet makes a list with only the odd elements of the squares list.

# Three-dimensional arrays
# Python does not limit the depth of list-in-list inclusion. Here you can see an example of a three-dimensional array:
# Imagine a hotel. It's a huge hotel consisting of three buildings, 15 floors each. There are 20 rooms on each floor.
# For this, you need an array which can collect and process information on the occupied/free rooms.
# First step - the type of the array's elements. In this case, a Boolean value (True/False) would fit.
# Step two - calm analysis of the situation. Summarize the available information: three buildings, 15 floors, 20 rooms.
# Now you can create the array:

rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

# The first index (0 through 2) selects one of the buildings; the second (0 through 14) selects
# the floor, the third (0 through 19) selects the room number. All rooms are initially free.
# Now you can book a room for two newlyweds: in the second building, on the tenth floor, room 14:

rooms[1][9][13] = True

# and release the second room on the fifth floor located in the first building:

rooms[0][4][1] = False

# Check if there are any vacancies on the 15th floor of the third building:

vacancy = 0

for roomNumber in range(20):
    if not rooms[2][14][roomNumber]:
        vacancy += 1

#########
#
# Key takeaways
#
# 1. List comprehension allows you to create new lists from existing ones in a concise and elegant way.
# The syntax of a list comprehension looks as follows:

[expression for element in list if conditional]

# which is actually an equivalent of the following code:

for element in list:
    if conditional:
        expression

# Here's an example of a list comprehension - the code creates a five-element list filled with with the first five natural numbers raised to the power of 3:

cubed = [num ** 3 for num in range(5)]
print(cubed) # outputs: [0, 1, 8, 27, 64]

# 2. You can use nested lists in Python to create matrices (i.e., two-dimensional lists). For example:


# A four-column/four-row table - a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0]) # outputs: ':('
print(table[0][3]) # outputs: ':)'

# 3. You can nest as many lists in lists as you want, and therefore create n-dimensional lists,
# e.g., three-, four- or even sixty-four-dimensional arrays. For example:
#
# Cube - a three-dimensional array

# Cube - a three-dimensional array (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0]) # outputs: ':('
print(cube[2][2][0]) # outputs: ':)'

##########################################################

# More on functions:

# PYTHON (BUILTIN)
# from Python itself - numerous functions (like print()) are an integral part of Python,
# and are always available without any additional effort on behalf of the programmer;
# we call these functions built-in functions;

# MODULES (IMPORTED)
# from Python's preinstalled modules - a lot of functions, very useful ones, but used significantly
# less often than built-in ones, are available in a number of modules installed together with Python;
# the use of these functions requires some additional steps from the programmer in order to make them
# fully accessible (we'll tell you about this in a while) (aka import of modules)

# CODE (DEFINED)
# directly from your code - you can write your own functions, place them inside your code, and use them freely;
# there is one other possibility, but it's connected with classes, so we'll omit it for now (using def)

# DEFINING A FUNCTION
# basic structure
def functionName():
    functionBody

# It always starts with the keyword def (for define)

# next after def goes the name of the function (the rules for naming functions are exactly the
# same as for naming variables)

# after the function name, there's a place for a pair of parentheses (they contain nothing here,
# but that will change soon) the line has to be ended with a colon;

# the line directly after def begins the function body - a couple (at least one) of
# necessarily nested instructions, which will be executed every time the function is invoked;
# note: the function ends where the nesting ends, so you have to be careful

# Function cannnot have the same name as any variable

# Example
# Defining new function called 'message'
def message():
    print("Enter a value: ")
# Using new function 3 times below for var a, b, c
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())

# Key takeaways
#
# 1. A function is a block of code that performs a specific task when the function is called
# (invoked). You can use functions to make your code reusable, better organized, and more readable.
# Functions can have parameters and return values.

# 2. There are at least four basic types of functions in Python:
# built-in functions which are an integral part of Python (such as the print() function).
# You can see a complete list of Python built-in functions at https://docs.python.org/3/library/functions.html.
# the ones that come from pre-installed modules (you'll learn about them in Module 5 of this course)
# user-defined functions which are written by users for users - you can write your own functions and use them
# freely in your code,

# 3. You can define your own function using the def keyword and the following syntax:

def yourFunction(optional parameters):
    # the body of the function

# You can define a function which doesn't take any arguments, e.g.:

def message():    # defining a function
    print("Hello")    # body of the function

message()    # calling the function

# You can define a function which takes arguments, too, just like the one-parameter function below:

def hello(name):    # defining a function
    print("Hello,", name)    # body of the function

name = input("Enter your name: ")

hello(name)    # calling the function

#######################

# Parametrized functions
# The function's full power reveals itself when it can be equipped with an interface that is
# able to accept data provided by the invoker. Such data can modify the function's behavior,
# making it more flexible and adaptable to changing conditions.
#
# A parameter is actually a variable, but there are two important factors that make parameters
# different and special:
#
# parameters exist only inside functions in which they have been defined, and the only place
# where the parameter can be defined is a space between a pair of parentheses in the def
# statement;
#
# assigning a value to the parameter is done at the time of the function's invocation, by
# specifying the corresponding argument.

# basic structure
def function(parameter):

# REMEMBER
# parameters live inside functions (this is their natural environment)
# arguments exist outside functions, and are carriers of values passed to corresponding parameters.

# Example - specifying 1 as the parameter
def message(number):
    print("Enter a number:", number)
message(1)

# Shows variable is different to specified parameter
def message(number):
    print("Enter a number:", number)
number = 1234
message(1)
print(number)

###########################

# Positional parameter passing

# A technique which assigns the ith (first, second, and so on) argument to the ith
# (first, second, and so on)
# function parameter is called positional parameter passing, while arguments passed
# in this way are named positional arguments.

# Keyword argument passing
#
# Python offers another convention for passing arguments, where the meaning of the
# argument is dictated by its name, not by its position - it's called keyword argument passing.
#
# Take a look at the snippet:

def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke")

# Mixing positional and keyword arguments
# You can mix both fashions if you want - there is only one unbreakable rule: you have to put
# positional arguments before keyword arguments.
#
# If you think for a moment, you'll certainly guess why.
#
# To show you how it works, we'll use the following simple three-parameter function:

def sum(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Key takeaways
#
# 1. You can pass information to functions by using parameters.
# Your functions can have as many parameters as you need.
#
# An example of a one-parameter function:

def hi(name):
    print("Hi,", name)

hi("Greg")

# An example of a two-parameter function:

def hiAll(name1, name2):
    print("Hi,", name2)
    print("Hi,", name1)

hiAll("Sebastian", "Konrad")

# An example of a three-parameter function:

def address(street, city, postalCode):
    print("Your address is:", street, "St.,", city, postalCode)

s = input("Street: ")
pC = input("Postal Code: ")
c = input("City: ")

address(s, c, pC)

# 2. You can pass arguments to a function using the following techniques:
#
# positional argument passing in which the order of arguments passed matters (Ex. 1),
# keyword (named) argument passing in which the order of arguments passed doesn't matter (Ex. 2),
# a mix of positional and keyword argument passing (Ex. 3).

# Ex. 1
def subtra(a, b):
    print(a - b)

subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3


# Ex. 2
def subtra(a, b):
    print(a - b)

subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3

# Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3

# It's important to remember that positional arguments mustn't follow keyword arguments.
# That's why if you try to run the following snippet:

def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(a=5, 2)    # Syntax Error

# Python will not let you do it by signalling a SyntaxError.

# 3. You can use the keyword argument passing technique to pre-define a value for a given argument:

def name(firstN, lastN="Smith"):
    print(firstN, lastN)

name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")






