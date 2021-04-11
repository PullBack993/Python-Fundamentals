from collections import defaultdict
num_heroes = int(input())

heroes = defaultdict(dict)

for num in range(num_heroes):
    data = input()
    hero, hp, mana = data.split()
    if hero not in heroes:
        heroes[hero] = defaultdict(int)
    heroes[hero]['hp_points'] += int(hp) #max 100
    heroes[hero]['mana_points'] += int(mana) #max 200

command = input()
while not command == 'End':
    command_name = command.split(" - ")
    hero_name = command_name[1]
    if command_name[0] == 'CastSpell':
        need_mana = command_name[2]
        spell_name = command_name[3]
        if heroes[hero_name]['mana_points'] >= int(need_mana):
            heroes[hero_name]['mana_points'] -= int(need_mana)
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana_points']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command_name[0] == 'TakeDamage':
        damage = command_name[2]
        attacker = command_name[3]
        heroes[hero_name]['hp_points'] -= int(damage)
        if heroes[hero_name]['hp_points'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp_points']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

    elif command_name[0] == 'Recharge':
        amount = command_name[2]
        heroes[hero_name]['mana_points'] += int(amount)
        if heroes[hero_name]['mana_points'] <= 200:
            print(f"{hero_name} recharged for {amount} MP!")
        else:
            difference = abs((heroes[hero_name]['mana_points'] - int(amount)) - 200)
            heroes[hero_name]['mana_points'] = 200
            print(f"{hero_name} recharged for {difference} MP!")

    elif command_name[0] == 'Heal':
        amount = command_name[2]
        heroes[hero_name]['hp_points'] += int(amount)
        if heroes[hero_name]['hp_points'] <= 100:
            print(f"{hero_name} healed for {amount} HP!")
        else:
            difference = abs((heroes[hero_name]['hp_points'] - int(amount)) - 100)
            heroes[hero_name]['hp_points'] = 100
            print(f"{hero_name} healed for {difference} HP!")
    command = input()

for heroes, hero_stats in sorted(heroes.items(), key=lambda x: (-x[1]['hp_points'], x)):
    print(f'{heroes}')
    print(f'HP: {hero_stats["hp_points"]}')
    print(f'MP: {hero_stats["mana_points"]}')