def happyNewYear(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")

# When invoked without any arguments:

happyNewYear()

# The function causes a little noise - the output will look like this:

# Three...
# Two...
# One...
# Happy New Year!

# Providing False as an argument:

happyNewYear(False)

# will modify the functions behavior - the return instruction will cause its termination
# just before the wishes - this is the updated output:

# Three...
# Two...
# One...