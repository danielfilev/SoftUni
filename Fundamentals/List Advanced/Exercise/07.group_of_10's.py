numbers = input().split(', ')
group_of_10s = [int(num) for num in numbers if int(num) <= 10]
groups_num = max(int(num) for num in numbers)
if groups_num % 10 == 0:
    groups_num = groups_num // 10
else:
    groups_num = groups_num // 10 + 1
print(f"Group of 10's: {group_of_10s}")
for gr in range(1, groups_num):
    result_list = []
    for num in numbers:
        if gr * 10 < int(num) <= (gr + 1) * 10:
            result_list.append(int(num))
    print(f"Group of {(gr + 1) * 10}'s: {result_list}")
