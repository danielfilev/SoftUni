numbers = input().split(" ")
numbers_list = list(map(int, numbers))


def even_check(num):
    if num % 2 == 0:
        return True

    return False


even_numbers_iterator = filter(even_check, numbers_list)
even_numbers = list(even_numbers_iterator)

print(even_numbers)
