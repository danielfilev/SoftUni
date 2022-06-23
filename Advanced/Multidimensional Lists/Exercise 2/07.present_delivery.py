def get_next_pos(row, col, command):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'left':
        return row, col - 1
    if command == 'right':
        return row, col + 1


def is_inside(row, col, n):
    return 0 <= row < n and 0 <= col <= n


def get_cookie_kids(matrix, row, col):

    result = []
    if is_inside(row - 1, col, len(matrix)) and matrix[row - 1][col] == "X" or matrix[row - 1][col] == "V":
        result.append([row-1, col])
    if is_inside(row + 1, col, len(matrix)) and matrix[row + 1][col] == "X" or matrix[row + 1][col] == "V":
        result.append([row+1, col])
    if is_inside(row, col - 1, len(matrix)) and matrix[row][col - 1] == "X" or matrix[row][col - 1] == "V":
        result.append([row, col-1])
    if is_inside(row, col + 1, len(matrix)) and matrix[row][col + 1] == "X" or matrix[row][col + 1] == "V":
        result.append([row, col+1])
    return result


presents = int(input())
n = int(input())

current_row = 0
current_col = 0
nice_kids = 0
kids_left = []
cookie_row = 0
cookie_col = 0

matrix = []
for row in range(n):
    row_elements = input().split()
    for col in range(n):
        if row_elements[col] == "S":
            current_row = row
            current_col = col
        elif row_elements[col] == "V":
            kids_left.append("V")
        elif row_elements[col] == "C":
            cookie_row = row
            cookie_col = col
    matrix.append(row_elements)


matrix[current_row][current_col] = "-"


while presents > 0:
    direction = input()

    if direction == "Christmas morning":
        break

    new_row, new_col = get_next_pos(current_row, current_col, direction)

    current_row, current_col = new_row, new_col

    if matrix[current_row][current_col] == "V":
        presents -= 1
        nice_kids += 1
        kids_left.remove("V")
    elif matrix[current_row][current_col] == "C":
        cookie_kids = get_cookie_kids(matrix, current_row, current_col)
        for kid_row, kid_col in cookie_kids:
            if matrix[kid_row][kid_col] == "V":
                nice_kids += 1
                kids_left.remove("V")
            matrix[kid_row][kid_col] = "-"
            presents -= 1
            if presents == 0:
                break

    matrix[current_row][current_col] = "-"


matrix[current_row][current_col] = "S"

if presents <= 0 and kids_left:
    print("Santa ran out of presents!")


for row in matrix:
    print(*row, sep=" ")

if presents >= 0 and not kids_left:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {len(kids_left)} nice kid/s.")
