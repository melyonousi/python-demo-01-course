# write a program that read various integers and stop when press enter, then display sum, max, min and average

numbers = []
counter = 1
while True:
    number = input(f"Enter number {counter}: ")
    counter += 1
    if number == "":
        break
    numbers.append(int(number))

print(f"number enter is: {numbers}")
print("sum: ", sum(numbers))
print("max: ", max(numbers))
print("min: ", min(numbers))
print("average: ", sum(numbers) / len(numbers))
