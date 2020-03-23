#BOOLEAN - if the result is true or flase

plant = input("Type in a really cool plant: ")

if plant == "Spathiphyllum":
    #In the case that the result of plant variable being Spathiphyllum then result is true so do the below (if not ignore and move to elif or else)
    print("Yes - Spathiphyllum is the best plant ever!")

elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum")

else:
    print("Spathiphyllum is cool, not a", plant)

    