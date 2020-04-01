# DEFINING FUNCTIONS EXAMPLES

# Definined function with positional parameter
def message(what, number):
    print("Enter", what, "number", number)

# invoke function (requires 2 parameters)
message("Jaffacakes", 300)

############################

# Definined function with positional parameter
def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")

##############################

# Defined function with keyword argument passing

def introduction(firstName, lastName):
    print("Hello, my name is", firstName, lastName)

introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke")

###############################

# Mixing positional paramter and keyword

def sum(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
sum(3, c = 1, b = 2)

###############################

# Specifying a default parameter (Smith)

def introduction(firstName, lastName="Smith"):
    print("Hello, my name is", firstName, lastName)

# call the function here
introduction(firstName="William")

###############################

# Defining function, then using list, for loop, insert and return
def strangeListFunction(n):
    strangeList = []

    for i in range(0, n):
        strangeList.insert(0, i)

    return strangeList

print(strangeListFunction(5))

# Returns [4, 3, 2, 1, 0]





