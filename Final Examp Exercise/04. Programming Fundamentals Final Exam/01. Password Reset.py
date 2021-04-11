password = input()
command = input()
box = ''
while not command == 'Done':
    command_split = command.split()
    name = command_split[0]
    if name == 'TakeOdd':
        for i in range(len(password)):
            if i % 2 == 1:
                box += password[i]
        password = box
        print(password)
    elif name == 'Cut':
        index = command_split[1]
        lenght = command_split[2]
        index = int(index)
        lenght = int(lenght)
        password = password[0:index] + password[index+lenght:]
        print(password)
    elif name == 'Substitute':
        sub_string = command_split[1]
        sub_stitute = command_split[2]
        if sub_string in password:
            password = password.replace(sub_string, sub_stitute)
            print(password)
        else:
            print("Nothing to replace!")

    command = input()
print(f"Your password is: {password}")