energy = int(input())
distance = input()
counter = 0
won_battles = 0
is_winner = True
while not distance == 'End of battle':
    distance = int(distance)

    if energy - distance >= 0:
        counter += 1
        won_battles += 1
        energy -= distance
        if counter == 3:
            energy += won_battles
            counter = 0
    else:
        is_winner = False
        print(f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy')
        break
    distance = input()

if is_winner:
    print(f'Won battles: {won_battles}. Energy left: {energy}')
