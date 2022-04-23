int1 = int(input())
int2 = int(input())
int3 = int(input())

if int1 > int2 and int1 > int3:
    print(int1)
elif int2 > int1 and int2 > int3:
    print(int2)
elif int3 > int2 and int3 > int1:
    print(int3)
