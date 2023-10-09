# write a program that calc prime numbers
# first method
import math


def isPrime1(a1):
    i1 = a1 - 1
    while True:
        if a1 % i1 == 0:
            return False
        i1 -= 1
        if i1 == 1:
            return True


a1 = int(input("Enter a number: "))

if isPrime1(a1):
    print(f"{a1} is prime")
else:
    print(f"{a1} is not prime")


# second method
def isPrime2(a2):
    if a2 % 1:
        return False
    i2 = 2
    if a2 % i2 == 0:
        return False
    while i2 < math.sqrt(a2):
        if a2 % i2 == 0:
            return False
        i2 += 2
    return True


a2 = int(input("Enter a number: "))
if isPrime2(a2):
    print(f"{a2} is prime")
else:
    print(f"{a2} is not prime")
