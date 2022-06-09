def read_matrix():
    rows = int(input())

    matrix = []
    for _ in range(rows):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    ll = []
    for row_index in matrix:
        ll += row_index

    return ll


print(read_matrix())
