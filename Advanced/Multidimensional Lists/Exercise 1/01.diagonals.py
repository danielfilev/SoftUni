def get_primary_diagonal_sum(matrix):
    primary_sum = []
    for i in range(n):
        primary_sum.append(matrix[i][i])
    return (
        f'Primary diagonal: {", ".join([str(x) for x in primary_sum])}. Sum: {sum(primary_sum)}')


def get_secondary_diagonal_sum(matrix):
    secondary_sum = []
    for i in range(n):
        secondary_sum.append(matrix[i][len(matrix) - i - 1])
    return (
        f'Secondary diagonal: {", ".join([str(x) for x in secondary_sum])}. Sum: {sum(secondary_sum)}')


n = int(input())
matrix = [[int(x) for x in input().split(', ')] for row in range(n)]

print(get_primary_diagonal_sum(matrix))
print(get_secondary_diagonal_sum(matrix))
