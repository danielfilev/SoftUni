def find_count(matrix, row, col):
    moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1]
    ]

    result = 0
    for r, c in moves:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == "K":
            result += 1
    return result


n = int(input())

matrix = [[x for x in input()] for row in range(n)]

deleted_knights = 0
while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == "0":
                continue
            count = find_count(matrix, row, col)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col

    if best_count == 0:
        break

    matrix[knight_row][knight_col] = '0'
    deleted_knights += 1

print(deleted_knights)
