def check_index_valid(index, targets):
    if index in range(targets):
        return True
    return False


targets = [int(n) for n in input().split()]

command = input()
while not command == 'End':
    name, index, power = command.split()
    index = int(index)
    power = int(power)
    if name == 'Shoot' and check_index_valid(index, len(targets)):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    elif name == 'Add':
        if check_index_valid(index, len(targets)):
            targets.insert(index, power)
        else:
            print('Invalid placement!')
    elif name == 'Strike':
        left_side = index - power
        right_side = index + power
        if 0 <= left_side <= len(targets) and 0 <= right_side <= len(targets):
            left_part = targets[:left_side]
            right_part = targets[right_side + 1:]
            targets = left_part + right_part
        else:
            print('Strike missed!')
    command = input()

print("|".join([str(i) for i in targets]))