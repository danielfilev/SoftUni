string1 = input().split(", ")
string2 = input().split(", ")
string3 = list()
for i in string1:
    for j in string2:
        if i in j:
            string3.append(i)
string3 = list(dict.fromkeys(string3))
print(string3)
