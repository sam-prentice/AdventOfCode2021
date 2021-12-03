from os import strerror


with open("input.txt", "r") as f:
    prev = 0
    increases = 0
    for line in f:
        stripped_line = int(line.rstrip("\n"))
        if prev == 0:
            prev = stripped_line
            continue
        if stripped_line > prev:
            increases += 1
        prev = stripped_line
    print("Number of increases: " + str(increases))

with open("input.txt", "r") as f:
    values = []
    for line in f:
        values.append(int(line.rstrip("\n")))
    
    i = 0
    j = 3
    previous_three_day_average = 0
    increases = 0

    while j <= len(values):
        selection = values[i:j]
        three_day_average = sum(selection)
        if previous_three_day_average == 0:
            previous_three_day_average = three_day_average
            continue
        if three_day_average > previous_three_day_average:
            increases += 1
        previous_three_day_average = three_day_average
        i += 1
        j += 1
    
    print("Number of increases: " + str(increases))