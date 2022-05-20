from collections import deque

queue = deque()

str = input()
while str != "End":
    if str == "Paid":
        while queue:
            print(queue.popleft())
    if str != "Paid":
        queue.append(str)
    str = input()

print(f"{len(queue)} people remaining.")
