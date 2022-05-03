todo = ["" for i in range(11)]

command = input()

while command != "End":
    explode = command.split("-")
    position = int(explode[0])
    task = explode[1]
    todo[position] = task

    command = input()
finished_todo = [i for i in todo if i != ""]
print(finished_todo)
