list_of_number = [int(number) for number in input().split(', ')]

group = 10
group_of_list = []
while list_of_number:
    for number in list_of_number:
        if group >= number:
            group_of_list.append(number)
    for n in group_of_list:
        list_of_number.remove(n)
    print(f"Group of {group}'s: {group_of_list}")
    group += 10
    group_of_list.clear()