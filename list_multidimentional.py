#This code won't work as the matrix is not being updated

# determine the monthly average noon temperature
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Average temperature at noon:", average)

# find the highest temperature during the whole month
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

highest = -100.0

for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp

print("The highest temperature was:", highest)

# count the days when the temperature at noon was at least 20 ℃
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#

hotDays = 0

for day in temps:
    if day[11] > 20.0:
        hotDays += 1

print(hotDays, "days were hot.")