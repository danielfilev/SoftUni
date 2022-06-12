def operate(operator, *args):

    def addition(x, *args):
        result = x
        for value in args:
            result += value
        return result

    def deduction(x, *args):
        return x + sum(-y for y in args)

    def multiplication(x, *args):
        result = x
        for value in args:
            result *= value
        return result

    def subtraction(x, *args):
        result = x
        for value in args:
            result /= value
        return result

    if operator == "+":
        return addition(*args)
    elif operator == "-":
        return deduction(*args)
    if operator == "*":
        return multiplication(*args)
    elif operator == "/":
        return subtraction(*args)


print(operate("/", 1, 2, 3, 4))
