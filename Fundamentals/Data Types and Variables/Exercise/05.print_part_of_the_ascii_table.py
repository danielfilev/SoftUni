x = int(input())
y = int(input())

for char in range(x, y+1):
    ascii_char = chr(char)
    print(f"{ascii_char} ", end="")
