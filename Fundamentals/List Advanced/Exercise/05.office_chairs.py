rooms = int(input())
total_chairs = 0
game_on = True

for room in range(1, rooms+1):
    command = input()
    explode = command.split(" ")
    if len(explode[0]) >= int(explode[1]):
        free_chairs = len(explode[0]) - int(explode[1])
        total_chairs += free_chairs
    else:
        missing_chair = int(explode[1]) - len(explode[0])
        print(f"{missing_chair} more chairs needed in room {room}")
        game_on = False


if game_on:
    print(f"Game On, {total_chairs} free chairs left")
