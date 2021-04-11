people_numbers = int(input())
registered_peoples = {}


for n in range(people_numbers):
    command = input().split()
    command_name = command[0]

    if command_name == 'register':
        name = command[1]
        license_number = command[2]
        if name not in registered_peoples:
            registered_peoples[name] = license_number
            print(f"{name} registered {license_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_number}")
    elif command_name == 'unregister':
        name = command[1]
        if name not in registered_peoples:
            print(f"ERROR: user {name} not found")
        else:
            registered_peoples.pop(name)
            print(f"{name} unregistered successfully")

for key, value in registered_peoples.items():
    print(f"{key} => {value}")