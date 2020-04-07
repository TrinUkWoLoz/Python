# 1 American mile = 1.609344 kilometres
# 1 American gallon = 3.785411784 litres

def l100kmtompg(str1, liters):
    gallons = liters / 3.785411784
    miles = 100 / 1.609344
    return miles / gallons


def mpgtol100km(str2, miles):
    liters = 3.785411784
    km = miles * 1.609344 / 100
    return liters / km


print(l100kmtompg("Miles per gallon:", 3.9))
print(l100kmtompg("Miles per gallon:", 7.5))
print(l100kmtompg("Miles per gallon:", 10.))
print(mpgtol100km("KM per gallon:", 60.3))
print(mpgtol100km("KM per gallon:", 31.4))
print(mpgtol100km("KM per gallon:", 23.5))

