lot = set()
n_cars = int(input())

for _ in range(n_cars):
    command, plate = input().split(', ')
    if command == "IN":
        lot.add(plate)
    elif command == "OUT":
        lot.remove(plate)

if lot:
    for car in lot:
        print(f'{car}')
else:
    print("Parking Lot is Empty")
