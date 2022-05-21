clothes = list(map(int, input().split()))
rack_capacity = int(input())
default = rack_capacity

n_racks = 0
while len(clothes) > 0:
    item = clothes.pop()
    if rack_capacity - item >= 0:
        rack_capacity -= item
    else:
        n_racks += 1
        rack_capacity = default
        clothes.append(item)
if rack_capacity < default and not clothes:
    n_racks += 1

print(n_racks)
