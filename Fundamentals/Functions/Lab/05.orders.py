order = input()
n = int(input())


def price(a, b):
    if order == "coffee":
        a = 1.50
    elif order == "water":
        a = 1.00
    elif order == "coke":
        a = 1.40
    elif order == "snacks":
        a = 2.00
    return a * b


result = price(order, n)
print(f"{result:.2f}")
