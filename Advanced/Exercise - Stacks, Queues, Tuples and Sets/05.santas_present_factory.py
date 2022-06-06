from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

presents_price = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

crafted_toys = {}

while materials and magic_values:
    material = materials.pop()
    value = magic_values.popleft()

    if material == 0 and value == 0:
        continue

    if material == 0:
        magic_values.appendleft(value)
        continue

    if value == 0:
        materials.append(material)
        continue

    result = material * value
    if result in presents_price:
        toy_name = presents_price[result]
        if toy_name in crafted_toys:
            crafted_toys[toy_name] += 1
        else:
            crafted_toys[toy_name] = 1
        continue

    if result < 0:
        materials.append(material + value)
    else:
        materials.append(material + 15)


if ('Doll' in crafted_toys and 'Wooden train' in crafted_toys) or ('Teddy bear' in crafted_toys and 'Bicycle' in crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(
        f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')

if magic_values:
    print(f'Magic left: {", ".join([str(x) for x in magic_values])}')

[print(f"{key}: {value}") for key, value in sorted(crafted_toys.items())]
