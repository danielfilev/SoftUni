rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

print([[x for x in row if x % 2 == 0] for row in matrix])
