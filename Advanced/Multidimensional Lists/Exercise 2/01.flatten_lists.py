data = [x for x in input().split('|')]

result = []

for idx in range(len(data) - 1, - 1, - 1):
    current_elements = data[idx].strip().split()
    result.extend(current_elements)

print(" ".join(result))
