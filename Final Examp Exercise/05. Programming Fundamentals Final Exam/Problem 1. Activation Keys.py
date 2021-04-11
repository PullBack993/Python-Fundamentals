activation_key = input()

command = input()


while not command == "Generate":
    command = command.split(">>>")
    name_command = command[0]
    if name_command == 'Contains':
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif name_command == "Flip":
        key = command[1]
        start_index = command[2]
        end_index = command[3]
        start_index = int(start_index)
        end_index = int(end_index)
        if key == 'Upper':
            new_party = activation_key[start_index:end_index].upper()
            activation_key = activation_key[0:start_index]+new_party + activation_key[end_index:]
            print(activation_key)
        elif key == "Lower":
            new_party = activation_key[start_index:end_index].lower()
            activation_key = activation_key[0:start_index] + new_party + activation_key[end_index:]
            print(activation_key)
    elif name_command == "Slice":
        start_index = command[1]
        end_index = command[2]
        start_index = int(start_index)
        end_index = int(end_index)
        activation_key = activation_key[0:start_index] + activation_key[end_index:]
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")
