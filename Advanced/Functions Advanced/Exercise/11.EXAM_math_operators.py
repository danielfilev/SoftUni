def math_operations(*args, **kwargs):

    operation_counter = 1
    for number in args:

        if operation_counter == 1:
            kwargs['a'] += number

        elif operation_counter == 2:
            kwargs['s'] -= number

        elif operation_counter == 3 and number != 0:
            kwargs['d'] /= number

        elif operation_counter == 4:
            kwargs['m'] *= number

        operation_counter += 1
        if operation_counter > 4:
            operation_counter = 1

    sorted_kwargs = [f"{key}: {value:.1f}"for key, value in sorted(
        kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))]

    return "\n".join(sorted_kwargs)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1,
                      s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-
                                                                    2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))

# After you finish calculating all numbers, sort the four elements by their values in descending order. If two or more values are equal, sort them by their keys in ascending order (alphabetically).
