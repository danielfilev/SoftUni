int1 = int(input())
int2 = int(input())
int3 = int(input())


def smallest_num():
    if int1 < int2 and int1 < int3:
        return int1
    elif int2 < int1 and int2 < int3:
        return int2
    elif int3 < int1 and int3 < int2:
        return int3


print(smallest_num())
