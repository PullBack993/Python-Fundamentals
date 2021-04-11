n = int(input())
grades = {}
for _ in range(n):
    name = input()
    grade = float(input())

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

filtered_grades = {}
for name, grade in grades.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.5:
        filtered_grades[name] = average_grade

first_student = sorted(filtered_grades.items(), key=lambda kvp: -kvp[1])
for student, avg in first_student:
    print(f'{student} -> {avg:.2f}')
