inventory = input().split(", ")

command = input()
while command != "Craft!":

    action = command.split(" - ")[0]
    item = command.split(" - ")[1]

    if action == "Collect":
        if item not in inventory:
            inventory.append(item)

    if action == "Drop":
        if item in inventory:
            inventory.remove(item)

    if action == "Combine Items":
        old_item = item.split(":")[0]
        new_item = item.split(":")[1]
        if old_item in inventory:
            index_old_item = inventory.index(old_item)
            inventory.insert(index_old_item + 1, new_item)

    if action == "Renew":
        if item in inventory:
            inventory.sort(key=item.__eq__)

    command = input()

print(*inventory, sep=", ")
