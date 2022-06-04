# 85/100, first test is a runtime error

from collections import deque

bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while bees and nectar:
    bee = bees.popleft()
    amount = nectar.pop()

    if amount < bee:
        bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    current_symbol = symbols.popleft()
    total_honey += abs(operations[current_symbol](bee, amount))


print(f"Total honey made: {total_honey}")
if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
if nectar:
    print(f'Nectar left: {", ".join([str(x) for x in nectar])}')
