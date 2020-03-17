#My Python Notes#

Created by Guido van Rossum (Dutch programmer)

Open source

Then developed continuosly by community

Additions Cython (C python) Rython (Reduced - subset of python for self development) & Jython (Java python)

Interpreter language such as Java Perl & Python

Compiler language C & Go (good for fast mathemeatical calculations)

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

1. The print() function is a built-in function. It prints/outputs a specified message to the screen/consol window.

2. Built-in functions, contrary to user-defined functions, are always available and don't have to be imported. Python 3.7.1 comes with 69 built-in functions. You can find their full list provided in alphabetical order in the Python Standard Library.

3. To call a function (function invocation), you need to use the function name followed by parentheses. You can pass arguments into a function by placing them inside the parentheses. You must separate arguments with a comma, e.g., print("Hello,", "world!"). An "empty" print() function outputs an empty line to the screen.

4. Python strings are delimited with quotes, e.g., "I am a string", or 'I am a string, too'.

5. Computer programs are collections of instructions. An instruction is a command to perform a specific task when executed, e.g., to print a certain message to the screen.

6. In Python strings the backslash (\) is a special character which announces that the next character has a different meaning, e.g., \n (the newline character) starts a new output line.

7. Positional arguments are the ones whose meaning is dictated by their position, e.g., the second argument is outputted after the first, the third is outputted after the second, etc.

8. Keyword arguments are the ones whose meaning is not dictated by their location, but by a special word (keyword) used to identify them.

9. The end and sep parameters can be used for formatting the output of the print() function. The sep parameter specifies the separator between the outputted arguments (e.g., print("H", "E", "L", "L", "O", sep="-"), whereas the end parameter specifies what to print at the end of the print statement.

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

#Can simplify by adding op to left side of operator
variable = variable op expression
x = x * 2

variable op= expression
x *= 2

############################

1. A variable is a named location reserved to store values in the memory. A variable is created or initialized automatically when you assign a value to it for the first time. (2.1.4.1)

2. Each variable must have a unique name - an identifier. A legal identifier name must be a non-empty sequence of characters, must begin with the underscore(_), or a letter, and it cannot be a Python keyword. The first character may be followed by underscores, letters, and digits. Identifiers in Python are case-sensitive. (2.1.4.1)

3. Python is a dynamically-typed language, which means you don't need to declare variables in it. (2.1.4.3) To assign values to variables, you can use a simple assignment operator in the form of the equal (=) sign, i.e., var = 1.

4. You can also use compound assignment operators (shortcut operators) to modify values assigned to variables, e.g., var += 1, or var /= 5 * 2. (2.1.4.8)

5. You can assign new values to already existing variables using the assignment operator or one of the compound operators, e.g.: (2.1.4.5)

var = 2
print(var)

var = 3
print(var)

var += 1
print(var)

6. You can combine text and variables using the + operator, and use the print() function to output strings and variables, e.g.: (2.1.4.4)

var = "007"
print("Agent " + var)

##############################

Key takeaways

1. Comments can be used to leave additional information in code. They are omitted at runtime. The information left in source code is addressed to human readers. In Python, a comment is a piece of text that begins with #. The comment extends to the end of line.

2. If you want to place a comment that spans several lines, you need to place # in front of them all. Moreover, you can use a comment to mark a piece of code that is not needed at the moment (see the last line of the snippet below), e.g.:

# This program prints
# an introduction to the screen.
print("Hello!")  # Invoking the print() function
# print("I'm Python.")

3. Whenever possible and justified, you should give self-commenting names to variables, e.g., if you're using two variables to store a length and width of something, the variable names length and width may be a better choice than myvar1 and myvar2.

4. It's important to use comments to make programs easier to understand, and to use readable and meaningful variable names in code. However, it's equally important not to use variable names that are confusing, or leave comments that contain wrong or incorrect information!

5. Comments can be important when you are reading your own code after some time (trust us, developers do forget what their own code does), and when others are reading your code (can help them understand what your programs do and how they do it more quickly).

########################

#INTEGER FUNCTION#
the int() function takes one argument (e.g., a string: int(string)) and tries to convert it into an integer;
if it fails, the whole program will fail too (there is a workaround for this situation, but we'll show you this a little later);

#FLOAT FUNCTION#
the float() function takes one argument (e.g., a string: float(string))and tries to convert it into a float (the rest is the same).

#########################

Key takeaways

1. The print() function sends data to the console, while the input() function gets data from the console.

2. The input() function comes with an optional parameter: the prompt string. It allows you to write a message before the user input, e.g.:

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

3. When the input() function is called, the program's flow is stopped, the prompt symbol keeps blinking (it prompts the user to take action when the console is switched to input mode) until the user has entered an input and/or pressed the Enter key.

NOTE

You can test the functionality of the input() function in its full scope locally on your machine. For resource optimization reasons, we have limited the maximum program execution time in Edube to a few seconds. Go to Sandbox, copy-paste the above snippet, run the program, and do nothing - just wait a few seconds to see what happens. Your program should be stopped automatically after a short moment. Now open IDLE, and run the same program there - can you see the difference?

Tip: the above-mentioned feature of the input() function can be used to prompt the user to end a program. Look at the code below:

name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")

3. The result of the input() function is a string. You can add strings to each other using the concatenation (+) operator. Check out this code:

num1 = input("Enter the first number: ") # Enter 12
num2 = input("Enter the second number: ") # Enter 21

print(num1 + num2) # the program returns 1221

4. You can also multiply (* - replication) strings, e.g.:

myInput = ("Enter something: ") # Example input: hello
print(myInput * 3) # Expected output: hellohellohello


######
OPERATORS
######

#MODULUS %
#Divide and check remainder dp

6%2

#Divide left by right
6/2 = 3
evaluates to 0 as there is no remainder

7%2

7/2=3.5
evaluates to 1 as there is 1dp remainder

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

         MODULE 3

###########################

#OPERATORS

= is an assignment operator, e.g., a = b assigns a with the value of b;

== is the question are these values equal?; a == b compares a and b

It is a binary operator with left-sided binding. It needs two arguments and checks if they are equal


Priority	   Operator
1	           +, -	            unary
2	           **
3	           *, /, //, %
4	           +, -	            binary
5	           <, <=, >, >=
6	           ==, !=

#Abreviation - using operators to print True/False result based on input and calc rule

Using one of the comparison operators in Python,
write a simple two-line program that takes the parameter n as input,
which is an integer, and prints False if n is less than 100,
and True if n is greater than or equal to 100

n = int(input("Enter your number: "))
print(n>=100)

#if statement

if true_or_not:
    do_this_if_true

This conditional statement consists of the following, strictly necessary, elements in this and this order only:

the if keyword;
one or more white spaces;
an expression (a question or an answer) whose value will be interpreted solely in terms of True (when its value is non-zero) and False (when it is equal to zero);
a colon followed by a newline;
an indented instruction or set of instructions (at least one instruction is absolutely required);
the indentation may be achieved in two ways - by inserting a particular number of spaces (the recommendation is to use four spaces of indentation),
or by using the tab character; note: if there is more than one instruction in the indented part, the indentation should be the same in all lines;
even though it may look the same if you use tabs mixed with spaces, it's important to make all indentations exactly the same -
Python 3 does not allow mixing spaces and tabs for indentation

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

    

















