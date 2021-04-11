targets = [int(str_target) for str_target in input().split()]

command = input()

while not command == 'End':
    data = command.split()
    word, index, value = data
    index, value = int(index), int(value)
    if word == 'Shoot':
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)

    elif word == 'Add':
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print(f'Invalid placement!')

    elif word == 'Strike':
        left_index = index - value
        right_index = index + value
        if left_index >= 0 and right_index < len(targets):
            left_part = targets[:left_index]
            right_part = targets[right_index + 1:]
            targets = left_part + right_part
        else:
            print("Strike missed!")
    command = input()

print('|'.join([str(el) for el in targets]))