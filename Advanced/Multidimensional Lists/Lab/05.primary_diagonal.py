matrix = []
rows = int(input())

for _ in range(rows):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

diagonal_sum = 0

for row_index in range(rows):
    for column_index in range(rows):
        if row_index == column_index:
            diagonal_sum += matrix[row_index][column_index]

print(diagonal_sum)
