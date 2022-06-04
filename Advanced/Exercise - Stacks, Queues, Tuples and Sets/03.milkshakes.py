from collections import deque

chocolates = [int(x) for x in input().split(', ')]
cups_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolates and cups_milk and milkshakes < 5:
    chocolate = chocolates.pop()
    milk = cups_milk.popleft()

    if chocolate <= 0 and milk <= 0:
        continue

    if chocolate <= 0:
        cups_milk.appendleft(milk)
        continue

    if milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        cups_milk.append(milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
    if chocolates:
        print(f'Chocolate: {", ".join([str(x) for x in chocolates])}')
    else:
        print("Chocolate: empty")

    if cups_milk:
        print(f'Milk: {", ".join([str(x) for x in cups_milk])}')
    else:
        print("Milk: empty")
else:
    print("Not enough milkshakes.")
