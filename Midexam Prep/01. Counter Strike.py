employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
student_count = int(input())

total_employers = employee_1 + employee_2 + employee_3

counter_time = 0
time = 0
while student_count > 0:
    if time == 3:
        counter_time += 1
        time = 0
        continue
    else:
        student_count -= total_employers
    time += 1
    counter_time += 1

print(f"Time needed: {counter_time}h.")