n = int(input())
table = set()

for _ in range(n):
    data = input()
    if " " in data:
        explode = data.split()
        for element in explode:
            table.add(element)
    else:
        table.add(data)

for i in table:
    print(i)
