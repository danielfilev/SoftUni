n_names = int(input())
dd = set()

for name in range(n_names):
    data = input()
    dd.add(name)

for name in dd:
    print(f"{name}")
