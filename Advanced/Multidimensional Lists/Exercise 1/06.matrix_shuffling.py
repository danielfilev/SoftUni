r, c = [int(x) for x in input().split()]

matrix = [[(x) for x in input().split()] for _ in range(r)]
last_value = 0

command = input()
while command != "END":
    explode = command.split()
    if "swap" in explode and len(explode) == 5:
        action, row1, col1, row2, col2 = explode[0], int(
            explode[1]), int(explode[2]), int(explode[3]), int(explode[4])
        if row1 in range(len(matrix)) and row2 in range(len(matrix)):
            if col1 in range(len(matrix[row1])) and col2 in range(len(matrix[row2])):
                last_value = matrix[row1][col1]
                matrix[row1][col1] = matrix[row2][col2]
                matrix[row2][col2] = last_value
                [print(f'{" ".join(matrix[i])}') for i in range(len(matrix))]
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()
