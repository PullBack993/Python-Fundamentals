encrypted_message = input()

command = input()

while not command == 'Decode':
    command_name = command.split("|")
    if command_name[0] == 'Move':
        num_of_letters = command_name[1]
        num_of_letters = int(num_of_letters)
        encrypted_message = encrypted_message[num_of_letters:] + encrypted_message[:num_of_letters]
    elif command_name[0] == 'Insert':
        index = command_name[1]
        value = command_name[2]
        index = int(index)
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif command_name[0] == 'ChangeAll':
        substring = command_name[1]
        replacement = command_name[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f'The decrypted message is: {encrypted_message}')