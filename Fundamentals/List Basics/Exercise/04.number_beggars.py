num_string = input()
beggars = int(input())

num_list = num_string.split(', ')
result_sum, result_list = 0, []

for n in range(beggars):
    for i in range(n, len(num_list), beggars):
        result_sum += int(num_list[i])
    result_list.append(result_sum)
    result_sum = 0

print(result_list)
