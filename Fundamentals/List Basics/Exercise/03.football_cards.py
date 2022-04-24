penalties = input().split(" ")
team_A = 11
team_B = 11
player_losses = []
condition = False

for penalty in penalties:
    if penalty not in player_losses:
        player_losses.append(penalty)
        if "A" in penalty:
            team_A -= 1
        elif "B" in penalty:
            team_B -= 1
        if team_A < 7 or team_B < 7:
            condition = True

print(f"Team A - {team_A}; Team B - {team_B}")
if condition:
    print("Game was terminated")
