n = int(input())
numbers = []
filtered = []

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered.append(number)

if command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered.append(number)

if command == "positive":
    for number in numbers:
        if number >= 0:
            filtered.append(number)

if command == "negative":
    for number in numbers:
        if number < 0:
            filtered.append(number)
print(filtered)
