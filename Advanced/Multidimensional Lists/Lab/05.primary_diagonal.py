matrix = []
rows = int(input())

for _ in range(rows):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]


print(diagonal_sum)
