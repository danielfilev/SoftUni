n = int(input())
total_sum = 0

for char in range(1, n+1):
    input1 = input()
    total_sum += ord(input1)
print(f"The sum equals: {total_sum}")
