def get_next_pos(row, col, command):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


n = int(input())
matrix = []

alice_row = 0
alice_col = 0

for row in range(n):
    row_elements = input().split()
    for col in range(n):
        if row_elements[col] == "A":
            alice_row = row
            alice_col = col
    matrix.append(row_elements)

tea_bags = 0

while tea_bags < 10:
    matrix[alice_col][alice_col] = '*'

    command = input()
    next_row, next_col = get_next_pos(alice_row, alice_col, command)

    if next_row < 0 or next_col < 0 or next_row >= n or next_col >= n:
        break

    alice_row, alice_col = next_row, next_col

    if matrix[alice_row][alice_col] == '.' or matrix[alice_row][alice_col] == '*':
        continue

    if matrix[alice_row][alice_col] == 'R':
        break

    tea_bags += int(matrix[alice_row][alice_col])

matrix[alice_col][alice_col] = '*'


if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=' ')
