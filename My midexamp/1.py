import math
budget = float(input())
students = int(input())
students_total = students
flour_price = float(input())
egg_price = float(input()) * 10 * students
apron_price = float(input())
counter_flour = 0
total_of_flour = 0
more_apron = math.ceil(students * 20 / 100) + students_total
total_of_apron = apron_price * more_apron
for n in range(students):
    counter_flour += 1
    if counter_flour == 5:
        total_of_flour += flour_price * 4
        counter_flour = 0
        students -= 5
if counter_flour < 5:
    total_of_flour += flour_price * students

all_price = total_of_apron + total_of_flour + egg_price

if all_price <= budget:
    print(f"Items purchased for {all_price:.2f}$.")
else:
    print(f"{all_price - budget:.2f}$ more needed.")