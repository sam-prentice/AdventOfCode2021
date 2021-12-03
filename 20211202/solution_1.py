with open("input.txt", "r") as f:

    command_list = []
    progress = 0
    depth = 0

    for line in f:
        command = line.rstrip("\n").split()
        command_list.append(command)

    for command in command_list:
        if command[0] == "forward":
            progress += int(command[1])

        if command[0] == "down":
            depth += int(command[1])

        if command[0] == "up":
            depth -= int(command[1])

    position_caluation = progress * depth
    print("Result: " + str(position_caluation))

with open("input.txt", "r") as f:

    aim = 0
    progress = 0
    depth = 0
    command_list = []

    for line in f:
        command = line.rstrip("\n").split()
        command_list.append(command)

    for command in command_list:
        if command[0] == "forward":
            progress += int(command[1])
            depth_adjustment = aim * int(command[1])
            depth += depth_adjustment

        if command[0] == "down":
            aim += int(command[1])

        if command[0] == "up":
            aim -= int(command[1])

    position_caluation = progress * depth
    print("Result: " + str(position_caluation))