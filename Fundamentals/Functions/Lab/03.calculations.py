operator = input()
a = int(input())
b = int(input())


def sum_func(a, b, operator):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


print(f"{sum_func(a, b, operator):.0f}")
