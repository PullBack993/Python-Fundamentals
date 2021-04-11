data = input()

while True:
    command_name = command = input().split()
    if command_name[0] == 'Done':
        break
    elif command_name[0] == "Change":
        char = command_name[1]
        replacement = command_name[2]
        data = data.replace(char, replacement)
        print(data)
    elif command_name[0] == 'Includes':
        string = command_name[1]
        if string in data:
            print("True")
        else:
            print("False")
    elif command_name[0] == 'End':
        string = command_name[1]
        if data.endswith(string):
            print('True')
        else:
            print('False')
    elif command_name[0] == 'Uppercase':
        data = data.upper()
        print(data)
    elif command_name[0] == 'FindIndex':
        char = command_name[1]
        for i in range(len(data)):
            if char in data[i]:
                print(i)
                break
    elif command_name[0] == 'Cut':
        start_index = command_name[1]
        length = command_name[2]
        start_index = int(start_index)
        length = int(length)
        start_cut = data[start_index:]
        end_cut = start_cut[:length]

        print(end_cut)