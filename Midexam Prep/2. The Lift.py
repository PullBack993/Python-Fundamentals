peoples = int(input())
wagons = [int(wagon) for wagon in input().split()]
for wagon in range(len(wagons)):
    difference = 4 - wagons[wagon]
    if peoples >= 4:
        wagons[wagon] += difference
        peoples -= difference
    elif peoples >= 0:
        wagons[wagon] += peoples
        peoples -= difference

try_to_sit = True
for wagon in wagons:
    if peoples > wagon:
        try_to_sit = True
    else:
        try_to_sit = False

if peoples == 0 and [wagon for wagon in wagons if wagon == 4]:
    print(f'{" ".join(str(wagon) for wagon in wagons)}')
    exit()
# if free_place:
if try_to_sit:
    print(f"There isn't enough space! {peoples} people in a queue!\n{' '.join(str(wagon) for wagon in wagons)}")
else:
    print(f"The lift has empty spots!\n{' '.join(str(wagon) for wagon in wagons)}")