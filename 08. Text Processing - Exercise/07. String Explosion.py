line = input()
index = 0
strength = 0
while index < len(line):
    if line[index] == ">" and line[index+1].isdigit():
        strength += int(line[index+1])
        index += 1
        while not line[index] == '>' and strength and not line[index+1].isdigit():
            if strength >= 2:
                line = line.replace(line[index], "", 1)
                strength -= 1
                index += 1
            else:
                line = line.replace(line[index], "", 1)
                strength -= 1
    else:
        index += 1
print(line)