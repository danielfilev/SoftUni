stack = []

n = int(input())

for _ in range(n):
    query = input()

    if query.startswith("1"):
        explode = query.split(" ")
        stack.append(int(explode[1]))
    elif query == "2" and stack:
        stack.pop()
    elif query == "3" and stack:
        print(max(stack))
    elif query == "4" and stack:
        print(min(stack))

ll = []
while stack:
    last_num = stack.pop()
    ll.append(last_num)
print(*ll, sep=", ")
