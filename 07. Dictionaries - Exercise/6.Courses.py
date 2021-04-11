course_list = {}
count = 0

command = input()

while not command == "end":
    course_name, student_name = command.split(" : ")

    if course_name not in course_list:
        course_list[course_name] = []
        course_list[course_name].append(student_name)
    else:
        course_list[course_name].append(student_name)

    command = input()

sorted_course_list = {x: sorted(course_list[x]) for x in course_list.keys()}
sorted_course_list = dict(sorted(sorted_course_list.items(), key=lambda x: len(x[1]), reverse=True))

for key, value in sorted_course_list.items():
    print(f"{key}: {len(value)}")
    for el in value:
        print(f"-- {el}")
