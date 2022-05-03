version = input().split(".")
version = list(map(int, version))

version[-1] += 1

if version[-1] + 1 > 9:
    version[1] += 1
    version[-1] = 0
    if version[1] > 9:
        version[0] += 1
        version[1] = 0


version = list(map(str, version))
print(".".join(version))
