gamma_list = [0,0,0,0,0,0,0,0,0,0,0,0]
epsilon_list = [0,0,0,0,0,0,0,0,0,0,0,0]

for x in range(0,12):
    zero = one = 0
    with open("input.txt", "r") as f:
        for line in f:
            if int(line[x]) == 0:
                zero += 1
            else:
                one += 1
        
        if one > zero :
            gamma_list[x] = 1
            epsilon_list[x] = 0
        else:
            gamma_list[x] = 0
            epsilon_list[x] = 1

gamma_string = ''.join([str(item) for item in gamma_list])
epsilon_string = ''.join([str(item) for item in epsilon_list])
power = int(gamma_string, 2) * int(epsilon_string, 2)
print("power: " + str(power))

file_in = open('input.txt')
data = file_in.read().splitlines()
file_in.close

o2Data = data
cO2Data = data

def find_most_common(index, data):
    zero = one = 0
    for i in data:
        if int(i[index]) == 0:
            zero += 1
        else:
            one += 1   
    if one >= zero:
        return 1
    else:
        return 0

def find_least_common(index, data):
    zero = one = 0
    for i in data:
        if int(i[index]) == 0:
            zero += 1
        else:
            one += 1
    
    if one >= zero:
        return 0
    else:
        return 1

def filter_list(reference, index, data):
    if len(data) > 1:
        new_data = [i for i in data if int(i[index]) == reference]
        return new_data
    else:
        return data

for x in range(12):
    o2Data = filter_list(find_most_common(x, o2Data), x, o2Data)
    cO2Data = filter_list(find_least_common(x, cO2Data), x, cO2Data)

print("Life support rating: " + str(int(o2Data[0], 2) * int(cO2Data[0], 2)))