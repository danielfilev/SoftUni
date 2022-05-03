
train_list = [0] * int(input())
command = input()

while command != "End":

    current_list = command.split()

    if "add" in command:
        train_list[-1] += int(current_list[1])
    if "insert" in command:
        train_list[int(current_list[1])] += int(current_list[2])
    if "leave" in command:
        train_list[int(current_list[1])] -= int(current_list[2])

    command = input()

print(train_list)
