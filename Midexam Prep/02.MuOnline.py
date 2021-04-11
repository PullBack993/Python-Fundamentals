data = input().split("|")

health = 100
health_2 = 0
bitcoins = 0
counter = 0
difference = 0
for d in data:
    command, number = d.split()
    number = int(number)
    counter += 1

    if command == 'potion':
        if health == 100:
            continue
        else:
            health_2 = health
            health += number
            if health > 100:
                difference = abs(health_2 - 100)
                health = 100
                print(f"You healed for {difference} hp.")
                print(f"Current health: {health} hp.")
            else:
                print(f"You healed for {number} hp.")
                print(f"Current health: {health} hp.")

    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')

    else:
        health -= number
        if health <= 0:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {counter}')
            break
        else:
            print(f'You slayed {command}.')

if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")