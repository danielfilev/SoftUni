nums = input().split(" ")
rounded_arr = []


def num_rounder():
    for i in range(len(nums)):
        nums[i] = float(nums[i])
        rounded_arr.append(round(nums[i]))
    return rounded_arr


print(num_rounder())
