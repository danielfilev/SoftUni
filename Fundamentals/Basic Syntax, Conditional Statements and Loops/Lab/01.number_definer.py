int1 = float(input())

if int1 == 0:
    print("zero")
elif int1 < 0:
    if abs(int1) < 1 and abs(int1) != 0:
        print("small negative")
    elif abs(int1) > 1 and abs(int1) < 1000000:
        print("negative")
    else:
        print("large negative")
elif int1 > 0:
    if abs(int1) < 1 and abs(int1) != 0:
        print("small positive")
    elif abs(int1) > 1 and abs(int1) < 1000000:
        print("positive")
    else:
        print("large positive")
