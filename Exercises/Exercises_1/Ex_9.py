# write a function that display a number factorial
# 5! = 4 * 3 * 2 * 1
# 0! = 1
# 1! = 1

def factorial(number_factorial):
    fact = 1
    if number_factorial == 0:
        fact = 1

    for i in range(1, number_factorial + 1):
        fact *= i
    return fact


n = int(input("Enter number factorial: "))

print(f"Number Factorial {n} is {factorial(n)}")
