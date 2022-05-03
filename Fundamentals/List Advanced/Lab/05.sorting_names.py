names = input().split(", ")
names.sort()


def len_list(e):
    return len(e)


names.sort(reverse=True, key=len_list)
print(names)
