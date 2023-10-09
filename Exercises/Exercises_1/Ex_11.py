# write a program that asks for two numbers from the user and display the LCM

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a * b / gcd(a, b))


a = int(input("Enter a Number: "))
b = int(input("Enter b Number: "))

print(f"the LCM {a} and {b} is {lcm(a, b)}")
