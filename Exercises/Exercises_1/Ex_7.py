# write a program that lets you solve a first-degree equation
# Ax + B = 0
#      A = 0 && B = 0 x from group R
#      A = B && B != 0 impossible equation
#      A != 0 x = -B / A

a = int(input("Enter A value: "))
b = int(input("Enter b value: "))

if a == 0:
    if b == 0:
        print("solution form group R")
    else:
        print("Group Vide => impossible Equation")
else:
    print("Solution x: ", -b/a)
