employees = [int(i) for i in input().split()]
happiness = int(input())
counter_not_happy = []
total_counter = [v*happiness for v in employees]
total_sum = sum(total_counter)//len(employees)
for i in total_counter:
    if i > total_sum:
        counter_not_happy.append(i)


if len(counter_not_happy) >= len(employees) // 2:
    print(f'Score: {len(counter_not_happy)}/{len(employees)}. Employees are happy!')

else:
    print(f'Score: {len(counter_not_happy)}/{len(employees)}. Employees are not happy!')