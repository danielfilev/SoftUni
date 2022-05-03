electrons = int(input())
sum_distributed = 0
list_electrons = list()

while electrons > sum_distributed:
    distrubtion = 2 * ((1 + len(list_electrons)) ** 2)
    if electrons - distrubtion < sum(list_electrons):
        list_electrons.append(electrons - sum(list_electrons))
        break
    list_electrons.append(distrubtion)
    sum_distributed += distrubtion

print(list_electrons)
