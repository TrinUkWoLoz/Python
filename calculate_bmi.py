#!/usr/bin/python3.7

def ftintom(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


def lbstokg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
            weight < 20 or weight > 200:
        return None

    return weight / height ** 2

# I am 175 lbs and 6 foot 2 inches - print my bmi
print("Laurence's BMI is:", bmi(weight=lbstokg(175), height=ftintom(6, 2)))

# Kim is 161 lbs and 5 foot 6 inches - print my bmi
print("Kim's BMI is:", bmi(weight=lbstokg(161), height=ftintom(5, 6)))

