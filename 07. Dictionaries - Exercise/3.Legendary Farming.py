data = input()
item = {'shards': 0, 'fragments': 0, 'motes': 0}
junk = {}
is_obtained = False
key_materials = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}

while not is_obtained:
    split_data = data.split()
    for i in range(0, len(split_data), 2):
        if is_obtained:
            break
        quantity = int(split_data[i])
        material = split_data[i + 1].lower()

        if material in item:
            item[material] += quantity
        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity

        for key,value in item.items():
            if value >= 250:
                item[key] -= 250
                is_obtained = True
                print(f'{key_materials[key]} obtained!')
                break

    if is_obtained:
        break
    data = input()

sorted_items = sorted(item.items(), key=lambda kvp: (-kvp[1], kvp[0]))
for material, quantity in sorted_items:
    print(f'{material}: {quantity}')

sorted_junks = sorted(junk.items(), key=lambda kvp: kvp[0])
for material, quantity in sorted_junks:
    print(f'{material}: {quantity}')