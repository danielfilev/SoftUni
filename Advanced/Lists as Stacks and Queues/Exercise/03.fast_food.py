from collections import deque


food_quantity = int(input())
order_quantity = input()

queue = deque(map(int, order_quantity.split(" ")))

print(max(queue))

for _ in range(len(queue)):
    order = queue[0]
    if food_quantity - order >= 0:
        food_quantity -= order
        queue.popleft()

if queue:
    print("Orders left:", *queue, sep=" ")
else:
    print("Orders complete")
