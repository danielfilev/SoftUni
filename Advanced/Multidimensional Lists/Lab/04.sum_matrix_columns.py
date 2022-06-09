def get_sum(matrix):
    column_sums = [0] * columns

    for row_index in range(rows):
        for column_index in range(columns):
            column_sums[column_index] += matrix[row_index][column_index]
    return column_sums


matrix = []
rows, columns = map(int, (input().split(', ')))

for _ in range(rows):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)


[print(x) for x in get_sum(matrix)]
