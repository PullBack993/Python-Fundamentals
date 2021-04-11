number_of_rooms = int(input())
taken_places = ""
number_of_people = 0
number_of_free_chairs = 0
all_seats_are_taken = True

for i in range(1, number_of_rooms + 1):
    chairs = input().split()
    taken_places = (chairs[0])
    number_of_people = (int(chairs[1]))
    if len(taken_places) == number_of_people:
        continue
    elif len(taken_places) > number_of_people:
        number_of_free_chairs += len(taken_places) - number_of_people
    elif len(taken_places) < number_of_people:
        all_seats_are_taken = False
        needed_chairs = number_of_people - len(taken_places)
        print(f"{needed_chairs} more chairs needed in room {i}")


if all_seats_are_taken:
    print(f"Game On, {number_of_free_chairs} free chairs left")