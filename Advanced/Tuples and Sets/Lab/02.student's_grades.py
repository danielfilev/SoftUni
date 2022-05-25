n_students = int(input())
dd = {}

for student in range(n_students):
    data = input().split(' ')
    name = data[0]
    grade = float(data[1])
    if name not in dd:
        dd[name] = []
    dd[name].append(grade)

for key, value in dd.items():
    value_formatted = ' '.join(f'{i:.2f}' for i in value)
    print(f"{key} -> {value_formatted} (avg: {sum(value) / len(value):.2f})")
