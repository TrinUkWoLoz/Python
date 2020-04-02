# Script to check if values (years) in list are leap years

def isYearLeap(year):
# A leap year is every 4 years, but not every 100 years, then again every 400 years
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

# Desired years to check
testData = [1900, 2000, 2016, 1987, 2020]
# Results of above calcs on values in list
testResults = [False, True, True, False, True]

for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    # if result == testResults[i]:
    #     print("OK")
    # else:
    #     print("Failed")
    if testResults[i] == True:
        print("This a leap year you fantastically clever beast!")
    else:
        print("This ain't no leap year chump muda *******!")

######WORKINGS#########

# 1900               ((True and False) or False)
#                        False or False
#                              False

# 2000               ((True and False) or True)
#                          False or True
#                               True

# 2016               ((True and True) or True)
#                          True or True
#                               True

# 1987               ((False and True) or False)
#                          False or False
#                               False

# 2020               ((True and True) or False)
#                          True or False
#                               True


