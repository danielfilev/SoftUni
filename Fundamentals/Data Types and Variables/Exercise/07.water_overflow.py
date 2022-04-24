n = int(input())
capacity = 255
total = 0

for line in range(n):
    litres = int(input())
    total += litres
    if total > capacity:
        print("Insufficent capacity!")
        total = total - litres
print(total)
