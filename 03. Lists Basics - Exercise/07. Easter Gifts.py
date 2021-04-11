list_of_gift = input().split()
command = input()

while not command == "No Money":
    current_command = command.split()
    current_gift = current_command[1]

    if current_command[0] == 'OutOfStock':
        for i in range(len(list_of_gift)):
            if list_of_gift[i] == current_gift:
                list_of_gift[i] = 'None'

    elif current_command[0] == 'Required':
        num = int(current_command[2])
        if 0 <= num < len(list_of_gift):
            list_of_gift[num] = current_gift

    elif current_command[0] == 'JustInCase':
        list_of_gift[-1] = current_gift

    command = input()
for gift in list_of_gift:
    if not gift == 'None':
        print(gift, end=' ')