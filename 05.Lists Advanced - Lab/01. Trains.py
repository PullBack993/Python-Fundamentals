wagons = int(input())

wagons_list = [0 for _ in range(wagons)]

command = input()

while not command == 'End':
    data = command.split()

    if data[0] == 'add':
        people = int(data[1])
        wagons_list[-1] += people
    elif data[0] == 'insert':
        index = int(data[1])
        people = int(data[2])
        wagons_list[index] += people
    elif data[0] == 'leave':
        index = int(data[1])
        people = int(data[2])
        wagons_list[index] -= people
    command = input()

print(wagons_list)