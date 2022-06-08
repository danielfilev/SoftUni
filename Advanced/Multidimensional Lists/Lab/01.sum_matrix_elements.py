def read_matrix():
    rows, columns = map(int, (input().split(', ')))

    matrix = []
    matrix_sum = 0
    for i in range(rows):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
        matrix_sum += sum(row)
    return matrix


matrix = read_matrix()
print(matrix)
