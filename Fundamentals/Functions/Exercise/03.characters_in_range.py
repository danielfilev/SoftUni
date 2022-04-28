def char_in_range(a, b):
    for char in range(ord(a) + 1, ord(b)):
        print(chr(char), end=" ")


a = input()
b = input()

char_in_range(a, b)
