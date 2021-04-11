sequence = [int(n) for n in input().split()]
shot = input()
counter = 0
while not shot == 'End':
    shot = int(shot)

    if shot not in range(len(sequence)):
        shot = input()
        continue
    counter += 1
    save_value_index_sequence = sequence[shot]

    if sequence[shot] == -1:
        shot = input()
        continue

    else:
        sequence[shot] = -1
        for index in range(len(sequence)):
            if sequence[index] == -1:
                continue
            if sequence[index] > save_value_index_sequence:
                sequence[index] -= save_value_index_sequence
            else:
                sequence[index] += save_value_index_sequence

        shot = input()
print(f'Shot targets: {counter} -> {" ".join([str(n) for n in sequence])}')