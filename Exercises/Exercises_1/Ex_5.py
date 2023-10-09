# write a program that ask a user for an integer and display their multiple table

number = int(input("Enter a number: "))

for i in range(11):
    if i != 0:
        print(f"{number} * {i} =  {int(i * number)}")
