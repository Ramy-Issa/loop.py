numbers = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
    value = int(input(f"number{i +1} = "))

    numbers.append(value)

print(numbers)

print(list(reversed(numbers)))