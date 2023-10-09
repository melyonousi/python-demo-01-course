# write a program that read 4 integers and display their sum, max, min and average

numbers = []
for i in range(4):
    numbers.append(int(input(f"Enter number {i + 1}: ")))

print(f"number enter is: {numbers}")
print("sum: ", sum(numbers))
print("max: ", max(numbers))
print("min: ", min(numbers))
print("average: ", sum(numbers) / len(numbers))
