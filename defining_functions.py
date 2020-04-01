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




