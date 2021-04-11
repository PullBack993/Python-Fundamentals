rooms = int(input())
free_chairs = 0
if_enough = True


for room in range(1, rooms+1):
    each_room = input().split()
    chairs = each_room[0]
    people_taken_places = int(each_room[1])
    if len(chairs) == people_taken_places:
        continue
    elif len(chairs) > people_taken_places:
        free_chairs += len(chairs) - people_taken_places
    else:
        if_enough = False
        print(f'{people_taken_places - len(chairs)} more chairs needed in room {room}')

if if_enough:
    print(f'Game On, {free_chairs} free chairs left')