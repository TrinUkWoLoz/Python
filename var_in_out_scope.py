# Let's start by checking whether or not a variable created outside any function is
# visible inside the functions. In other words, does a variable's name propagate
# into a function's body?

def myFunction():
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

# Look at the code in the editor. Our guinea pig is there.
# The result of the test is positive - the code outputs:
#
# Do I know that variable? 1
# 1

# The answer is: a variable existing outside a function has a scope inside the
# functions' bodies.
# This rule has a very important exception. Let's try to find it.
# Let's make a small change to the code:

def myFunction():
    var = 2
    print("Do I know that variable?", var)

var = 1
myFunction()
print(var)

# The result has changed, too - the code produces a slightly different output now:
#
# Do I know that variable? 2
# 1

