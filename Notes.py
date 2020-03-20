#My Python Notes#

#Created by Guido van Rossum (Dutch programmer)

#Open source

#Then developed continuosly by community

#Additions Cython (C python) Rython (Reduced - subset of python for self development) & Jython (Java python)

#Interpreter language such as Java Perl & Python

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

#Bitwise operations (&, |, and ^)
#   Arg A	Arg B	Arg B & Arg B	Arg A | Arg B	Arg A ^ Arg B
#   0	    0	        0	            0	                0
#   0	    1	        0	            1	                1
#   1	    0	        0	            1	                1
#   1	    1	        1	            1	                0

#Bitwise operations (~)
#   Arg	    ~Arg
#   0	      1
#   1	      0

#   & requires exactly two 1s to provide 1 as the result;
#   | requires at least one 1 to provide 1 as the result;
#   ^ requires exactly one 1 to provide 1 as the result.

