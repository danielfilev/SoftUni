r, c = [int(x) for x in input().split()]

matrix = []
for i in range(r):
    for j in range(c):
        print(chr(97 + i) + chr(97 + i + j) + chr(97 + i), end=" ")
    print()
