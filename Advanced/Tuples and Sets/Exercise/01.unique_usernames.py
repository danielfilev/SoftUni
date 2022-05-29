n_names = int(input())
unique = set()

for i in range(n_names):
    name = input()
    unique.add(name)

for name in unique:
    print(name)
