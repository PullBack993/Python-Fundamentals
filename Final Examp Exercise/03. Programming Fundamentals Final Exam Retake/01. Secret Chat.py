concealed_message = input()

command = input()

while not command == 'Reveal':
    command_name = command.split(":|:")
    if command_name[0] == 'InsertSpace':
        index = int(command_name[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index::]
    elif command_name[0] == "Reverse":
        substring = command_name[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, "", 1)
            revers_subst = substring[::-1]
            concealed_message = concealed_message + revers_subst
        else:
            print('error')
            command = input()
            continue
    elif command_name[0] == 'ChangeAll':
        substring = command_name[1]
        replacement = command_name[2]
        concealed_message = concealed_message.replace(substring, replacement)
    print(concealed_message)
    command = input()
print(f"You have a new text message: {concealed_message}")