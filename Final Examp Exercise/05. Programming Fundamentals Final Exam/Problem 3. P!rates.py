cities = input()
cities_dict = {}

while not cities == 'Sail':
    city, people, gold = cities.split("||")
    people = int(people)
    gold = int(gold)
    if city in cities_dict:
        people_plus, gold_plus = cities_dict[city]
        people_plus += people
        gold_plus += gold
        cities_dict[city] = [people_plus, gold_plus]
    else:
        cities_dict[city] = [people, gold]

    cities = input()

actions = input()
while not actions == "End":
    actions_split = actions.split("=>")
    name = actions_split[0]
    if name == 'Plunder':
        town = actions_split[1]
        citizen = actions_split[2]
        money = actions_split[3]
        citizen = int(citizen)
        money = int(money)
        if town in cities_dict:
            citizens, golds = cities_dict[town]
            citizens -= citizen
            golds -= money
            print(f"{town} plundered! {money} gold stolen, {citizen} citizens killed.")
            if golds <= 0 or citizens <= 0:
                cities_dict.pop(town)
                print(f"{town} has been wiped off the map!")
            else:
                cities_dict[town] = [citizens, golds]
        actions = input()
    elif name == 'Prosper':
        add_gold_town = actions_split[1]
        add_gold = actions_split[2]
        add_gold = int(add_gold)
        if add_gold < 0:
            actions = input()
            print(f"Gold added cannot be a negative number!")
            continue
        else:
            key, value = cities_dict[add_gold_town]
            value += add_gold
            cities_dict[add_gold_town] = [key, value]
            print(f"{add_gold} gold added to the city treasury. {add_gold_town} now has {value} gold.")
        actions = input()
if cities_dict:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    cities_dict = dict(sorted(cities_dict.items(), key=lambda kvp: (- kvp[1][1], kvp[0])))
    for target, value in cities_dict.items():
        print(f"{target} -> Population: {cities_dict[target][0]} citizens, Gold: {cities_dict[target][1]} kg")
else:
    print(f'Ahoy, Captain! All targets have been plundered and destroyed!')