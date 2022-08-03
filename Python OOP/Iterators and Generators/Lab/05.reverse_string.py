def reverse_text(string):
    n = -1
    while n >= -len(string):
        yield string[n]
        n -= 1


for char in reverse_text("step"):
    print(char, end='')
# output should be: "pets"
