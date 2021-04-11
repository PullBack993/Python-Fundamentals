init_list = input().split("!")
command = input()

while not command == "Go Shopping!":
    new_command = command.split()
    order = new_command[0]
    item = new_command[1]

    if order == "Urgent":
        if item not in init_list:
            init_list.insert(0, item)

    elif order == "Unnecessary":
        if item in init_list:
            init_list.remove(item)

    elif order == "Correct":
        if item in init_list:
            for idx, ob in enumerate(init_list):
                if ob == item:
                    init_list[idx] = new_command[2]
                    break

    elif order == "Rearrange":
        if new_command[1] in init_list:
            init_list.remove(item)
            init_list.append(item)

    command = input()
    if command == "Go Shopping!":
        print(", ".join(init_list))
        break