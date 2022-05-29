data = list(map(int, input().split(' ')))
target = int(input())
iterations = 0
pairs = set()

for main_index in range(len(data)):
    for second_index in range(main_index+1, len(data)):
        iterations += 1
        if data[main_index] + data[second_index] == target:
            current_pair = (data[main_index], data[second_index])
            pairs.add(current_pair)
            print(f"{data[main_index]} + {data[second_index]} = {target}")

print(f'Iterations done: {iterations}')
for pair in pairs:
    print(pair)
