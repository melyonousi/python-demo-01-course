# write a program that lets you solve a second-degree equation
# Axx + Bx + C = 0
#      A = 0 && B = 0 && C = 0 x from group R
#      A = 0 && B = 0 && C != 0 impossible equation
#      A = 0 && B != 0 x = -C / B
#      A != 0
#           delta = bb - 4ac
#               delta = 0
#                       x1 = x2 = -B / 2A
#               delta > 0
#                       x1 = -B - sqrt(delta) / 2A
#                       x2 = B - sqrt(delta) / 2A
#               delta < 0 solve impossible in A
import math

A = int(input("Enter A value: "))
B = int(input("Enter b value: "))
C = int(input("Enter b value: "))

if A == 0:
    if B == 0:
        if C == 0:
            print("solution form group R")
        else:
            print("impossible equation")
    else:
        print("Solution x: ", -C / B)
else:
    delta = math.pow(B, 2) - (4 * A * C)
    if delta == 0:
        print("Solution x: ", -B / (2 * A))
    elif delta < 0:
        print("solve impossible in A")
    else:
        print("Solution x1: ", -B - math.sqrt(delta) / (2 * A))
        print("Solution x2: ", B - math.sqrt(delta) / (2 * A))