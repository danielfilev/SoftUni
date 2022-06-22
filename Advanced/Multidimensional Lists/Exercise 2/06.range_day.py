def get_next_pos(row, col, command, steps):
    if command == 'up':
        return row - steps, col
    if command == 'down':
        return row + steps, col
    if command == 'left':
        return row, col - steps
    if command == 'right':
        return row, col + steps


def is_inside(row, col, matrix):
    if 0 <= row < len(matrix) and 0 <= col <= len(matrix):
        return True
    return False


def seeking_target(row, col, command):

    if command == "up":
        travel = 0
        target = matrix[row - travel][col]
        while target != "x":
            target = matrix[row - travel][col]
            if target != "x":
                travel += 1
            else:
                row = [row - travel]
                col = [col]
                break
        return row, col


current_row = 0
current_col = 0
targets = 0

matrix = []
for row in range(5):
    row_elements = input().split()
    for col in range(5):
        if row_elements[col] == "A":
            current_row = row
            current_col = col
        elif row_elements[col] == "x":
            targets += 1
    matrix.append(row_elements)

shot_targets = []
matrix[current_row][current_col] = "."

n_commands = int(input())
for _ in range(n_commands):
    action = input().split()
    direction = action[1]

    if action[0] == "move":
        steps = int(action[2])

        next_row, next_col = get_next_pos(
            current_row, current_col, direction, steps)

        if is_inside(next_row, next_col, matrix) and matrix[next_row][next_col] == ".":
            current_row, current_col = next_row, next_col

    elif action[0] == "shoot":

        bullet_row, bullet_col = get_next_pos(
            current_row, current_col, direction, 1)
        while is_inside(bullet_row, bullet_col, matrix):
            if matrix[bullet_row][bullet_col] == "x":
                targets -= 1
                shot_targets.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = "."
                break
            bullet_row, bullet_col = get_next_pos(
                bullet_row, bullet_col, direction, 1)
        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")

print(*shot_targets, sep="\n")
