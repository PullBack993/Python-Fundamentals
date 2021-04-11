force_book = {}

while True:
    user_in_force = False
    command = input()
    if command == 'Lumpawaroo':
        break
    if ' | ' in command:
        side, user = command.split(' | ')
        if side not in force_book:
            force_book[side] = []
            for side, users in force_book.items():
                for u in users:
                    if u == user:
                        user_in_force = True
                        break
                if user_in_force:
                    break
            if user_in_force:
                continue
        if user not in force_book[side]:
            force_book[side].append(user)
    elif ' -> ' in command:
        user, side = command.split(' -> ')
        if side not in force_book:
            force_book[side] = []
        if user not in force_book[side]:
            force_book[side].append(user)
            for s, users in force_book.items():
                if s not in side:
                    while user in users:
                        force_book[s].remove(user)

            print(f'{user} joins the {side} side!')


for side, users in sorted(force_book.items(), key=lambda x: (-len(x[1]), x[0])):
    if users:
        print(f'Side: {side}, Members: {len(users)}')
    for user in sorted(users):
        print(f'! {user}')