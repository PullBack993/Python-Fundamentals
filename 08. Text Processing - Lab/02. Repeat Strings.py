data = input().split()
new_line = ''
for i in range(len(data)):
    new_line += data[i] * len(data[i])
print(new_line)