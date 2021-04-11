shopping_list = input().split('!')
command = input()
while not command == 'Go Shopping!':
    command = command.split()

    if command[0] == 'Urgent':
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])

    elif command[0] == 'Unnecessary':
        if command[1] in shopping_list:
            shopping_list.remove(command[1])

    elif command[0] == 'Correct':
        if command[1] in shopping_list:
            old_item = shopping_list.index(command[1])
            shopping_list[old_item] = command[2]

    elif command[0] == 'Rearrange':
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])

    command = input()
if command == 'Go Shopping!':
    print(f"{', '.join(shopping_list)}")
