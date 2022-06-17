n = int(input())
matrix = [[int(x) for x in input().split()] for x in range(n)]

command = input()
while command != "END":
    explode = command.split()
    if explode[0] == "Add":
        if int(explode[1]) < len(matrix) and int(explode[2]) < len(matrix[int(explode[1])]) and int(explode[1]) > -1 and int(explode[2]) > -1:
            matrix[int(explode[1])][int(explode[2])] += int(explode[3])
        else:
            print("Invalid coordinates")
    else:
        if int(explode[1]) < len(matrix) and int(explode[2]) < len(matrix[int(explode[1])]) and int(explode[1]) > -1 and int(explode[2]) > -1:
            matrix[int(explode[1])][int(explode[2])] -= int(explode[3])
        else:
            print("Invalid coordinates")

    command = input()

for row in matrix:
    print(*row, end="\n")
