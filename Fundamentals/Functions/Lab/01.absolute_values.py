sequence = input().split(" ")
abs_list = []


def abs_values():
    for i in range(len(sequence)):
        sequence[i] = abs(float(sequence[i]))
        abs_list.append(sequence[i])
    print(abs_list)


abs_values()
