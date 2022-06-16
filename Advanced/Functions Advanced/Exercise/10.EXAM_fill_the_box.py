def fill_the_box(h, l, w, *args):
    box_size = h * l * w
    left_cubes = 0

    for el in args:

        if el == "Finish":
            break

        if box_size >= el:
            box_size -= el
        else:
            el -= box_size
            left_cubes += el
            box_size = 0

    if box_size > 0:
        return f"There is free space in the box. You could put {box_size} more cubes."
    return f"No more free space! You have {left_cubes} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print()
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
