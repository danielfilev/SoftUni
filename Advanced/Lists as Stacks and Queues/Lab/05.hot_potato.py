from collections import deque


kids_string = input()
n_tosses_str = int(input())

kids = deque(kids_string.split(" "))
n_tosses = int(n_tosses_str)

current_count = 0
while len(kids) > 1:
    current_count += 1

    kid = kids.popleft()

    if current_count < n_tosses:
        kids.append(kid)

    else:
        print(f"Removed {kid}")
        current_count = 0

print(f"Last is {kids.popleft()}")
