def even_odd(*args):
    even = [int(x) for x in args[:-1] if x % 2 == 0]
    odd = [int(x) for x in args[:-1] if x % 2 != 0]
    if args[-1] == "even":
        return even
    return odd


print(even_odd(1, 2, 3, 4, 5, 6, "odd"))
