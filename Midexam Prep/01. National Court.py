first_employer = int(input())
second_employer = int(input())
third_employer = int(input())
people_counter = int(input())

total_employers = first_employer + second_employer + third_employer

counter_time = 0
time = 0
while people_counter > 0:
    if time == 3:
        counter_time += 1
        time = 0
        continue
    else:
        people_counter -= total_employers
    time += 1
    counter_time += 1

print(f"Time needed: {counter_time}h.")