array = [int(n) for n in input().split()]
command = input()
while not command == 'end':
    split_command = command.split()
    name = split_command[0]
    if name == 'swap':
        index_1 = int(split_command[1])
        index_2 = int(split_command[2])
        array[index_1], array[index_2] = array[index_2], array[index_1]

    elif name == 'multiply':
        index_1 = int(split_command[1])
        index_2 = int(split_command[2])
        sum_of_multiply = array[index_1] * array[index_2]
        array[index_1] = sum_of_multiply
        # array.insert(index_1, sum_of_multiply)
        # remove_number = array[index_1]
        # array[remove_number] = sum_of_multiply
    elif name == 'decrease':

        array = [x - 1 for x in array]

    command = input()
array = [str(num) for num in array]
print(f"{', '.join(array)}")