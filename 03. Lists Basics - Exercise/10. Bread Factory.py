ENERGY = 100
COINS = 100

working_day_events = input().split('|')
coast = 0
for day in working_day_events:
    event_name, number = day.split('-')
    number = int(number)
    if event_name == 'rest':
        if ENERGY >= 100:
            print(f'You gained 0 energy.')
            print(f'Current energy: {ENERGY}.')
            continue
        else:
            ENERGY += 10
            print(f'You gained {number} energy.')
            print(f'Current energy: {ENERGY}.')
    if event_name == 'order':
        if ENERGY >= 30:
            ENERGY -= 30
            COINS += number
            print(f'You earned {number} coins.')
        else:
            ENERGY += 50
            print(f'You had to rest!')
            continue
    if event_name != 'order' and event_name != 'rest':
        if COINS <= number:
            coast = number
            print(f"Closed! Cannot afford {event_name}.")
            break
        else:
            COINS -= number
            print(f'You bought {event_name}.')

if COINS > coast:
    print(f'Day completed!')
    print(f'Coins: {COINS}')
    print(f"Energy: {ENERGY}")