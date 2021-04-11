number = input().split(', ')
beggars = int(input())
counter = []
start_index = 0

for beggar in range(beggars):
    current_sum = 0
    for i in range(start_index, len(number), beggars):
        current_sum += int(number[i])
    counter.append(current_sum)
    start_index += 1
print(counter)