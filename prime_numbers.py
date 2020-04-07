def isPrime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num == 3:
        return True
    else:
        # this loop to check % from 2 to num-1. If its result=0 ==> False and break. Else True
        for i in range(2, num):  # Ex: num is 15,when it %5, result=0. So it must false and break.
            if num % i == 0:
                return False
                break
        else:
            return True


for i in range(1, 1000):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()

