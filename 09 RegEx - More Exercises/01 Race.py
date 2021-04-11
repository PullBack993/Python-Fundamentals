import re
participants = input().split(", ")
participants = {name: 0 for name in participants}
data = input()
name = r"[A-Za-z]+"
distance = r'\d'
while not data == 'end of race':
    name_person = re.findall(name, data)
    distance_person = re.findall(distance, data)
    name_person = "".join(name_person)
    distance_person = sum(map(int, distance_person))
    if name_person in participants:
       participants[name_person] += distance_person

    data = input()


counter = 0
while not counter == 3:
    race_dict = sorted(participants.items(), key=lambda kvp: -kvp[1])
    print(f'{counter+1}st place: {race_dict[0][0]}')
    race_dict.pop(0)
    counter += 1
    print(f'{counter+1}nd place: {race_dict[0][0]}')
    race_dict.pop(0)
    counter += 1
    print(f'{counter + 1}rd place: {race_dict[0][0]}')
    race_dict.pop(0)
    counter += 1