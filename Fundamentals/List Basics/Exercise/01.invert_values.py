string1 = input().split()
list1 = list()
for i in string1:
    if int(i) > 0:
        list1.append(-int(i))
    else:
        list1.append(abs(int(i)))
print(list1)
