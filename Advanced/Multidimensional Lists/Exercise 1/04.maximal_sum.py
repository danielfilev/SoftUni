rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

best_sum = float('-inf')
for row in range(rows-2):
    for column in range(columns-2):
        current_sum = matrix[row][column] + \
            matrix[row][column+1] + matrix[row][column+2] + \
            matrix[row+1][column] + matrix[row+2][column] + \
            matrix[row+1][column+1] + matrix[row + 2][column+2] + \
            matrix[row+1][column+2] + matrix[row+2][column + 1]
        if current_sum > best_sum:
            best_sum = current_sum
            start_row = row
            start_col = column

print(f"Sum = {best_sum}")
print(f"{matrix[row][column]} {matrix[row][column+1]} {matrix[row][column+2]}")
print(
    f"{matrix[row+1][column]} {matrix[row+1][column+1]} {matrix[row+1][column+2]}")
print(
    f"{matrix[row+2][column]} {matrix[row+2][column+1]} {matrix[row+2][column+2]}")
