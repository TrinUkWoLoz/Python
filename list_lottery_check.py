# List lottery check
# Checks numbers: 3, 7, 11, 42, 34, 49 against drawn numbers
# If number is hit then add to hits value (0)

drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits)


