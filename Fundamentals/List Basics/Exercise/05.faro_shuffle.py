deck = input().split(" ")
shuffles = int(input())

length = len(deck)
mid = int(length / 2)

for i in range(shuffles):
    list1 = []
    for p in range(mid):
        list1.append(deck[p])
        list1.append(deck[mid])
        mid += 1
    deck = list1
    mid = int(length / 2)

print(list1)
