n = int(input())
matrix = [list(input()) for _ in range(n)]
symbol = input()
is_found = False

for row in range(len(matrix)):
    if is_found:
        break
    for column in range(len(matrix)):
        if matrix[row][column] == symbol:
            print(f"({row}, {column})")
            is_found = True
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")
