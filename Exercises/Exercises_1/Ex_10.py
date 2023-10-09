# write a program that asks for two numbers from the user and display the GCD

first_number = int(input("Enter first Number: "))
second_number = int(input("Enter second Number: "))

if first_number < second_number:
    first_number, second_number = second_number, first_number

# first method
x = second_number
while True:
    if first_number % x == 0 and second_number % x == 0:
        break
    x -= 1
print(f"the GCD {first_number} and {second_number} is {x}")


# ========= second method =========
def gcd(a, b):
    if b == 0:
        return a
    else:
        print(f"a % b: {a % b}, a: {a}, b: {b}, GCD: {gcd(b, a % b)}")
        return gcd(b, a % b)


a = int(input("Enter a Number: "))
b = int(input("Enter b Number: "))

print(f"the GCD {a} and {b} is {gcd(a, b)}")
