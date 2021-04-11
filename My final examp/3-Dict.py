users = {}

while True:
    data = input()
    if data == 'Log out':
        break
    name_command = data.split(": ")
    name = name_command[0]
    if name.startswith('New'):
        user_name = name_command[1]
        if user_name in users:
            pass
        else:
            users[user_name] = []
    elif name.startswith("Like"):
        user_name = name_command[1]
        count = name_command[2]
        if user_name in users:
            users[user_name].append(count)
        else:
            users[user_name] = [count]
    elif name.startswith('Comment'):
        user_name = name_command[1]
        if user_name in users:
            users[user_name] += ['1']
        else:
            users[user_name] = ['1']
    elif name.startswith('Blocked'):
        user_name = name_command[1]
        if user_name in users:
            del users[user_name]
        else:
            print(f"{user_name} doesn't exist.")

all_sum = 0
for key, value in users.items():
    for v in value:
        all_sum += int(v)
    users[key] = all_sum
    all_sum = 0

sorted_dict = sorted(users.items(), key=lambda kvp: (-kvp[1], kvp[0]))
print(f"{len(sorted_dict)} followers")

for k, v in sorted_dict:
    print(f'{k}: {v}')