party_size = int(input())
days = int(input())

party = party_size
coins = 0

for day in range(1, days + 1):

    if day % 15 == 0:
        party += 5
    if day % 10 == 0:
        party -= 2
    if day % 5 == 0:
        coins += 20 * party
        if day % 3 == 0:
            coins -= party * 2
    if day % 3 == 0:
        coins -= party * 3

    coins += 50 - (party * 2)

print(f"{party} companions received {coins // party} coins each.")
