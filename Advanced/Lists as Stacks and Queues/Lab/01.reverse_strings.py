str = input()
ll = [i for i in str]
stack = []

for i in ll:
    stack.append(i)

reversed_str = ""

while stack:
    reversed_str += stack.pop()


print(reversed_str)
