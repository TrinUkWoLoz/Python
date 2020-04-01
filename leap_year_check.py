# Script to check if values (years) in list are leap years

def isYearLeap(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")

# 1900               ((True and False) or False)
#                        False or Flase
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