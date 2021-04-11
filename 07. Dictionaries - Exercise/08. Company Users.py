command = input()
company_users = {}
while not command == 'End':
    company, id = command.split(" -> ")

    if company not in company_users:
        company_users[company] = [id]
    else:
        if id in company_users:
            command = input()
        company_users[company].append(id)

    command = input()

sorted_list = []
sorted_company = sorted(company_users.items(), key=lambda x: x[0])
for key, value in sorted_company:
    print(f"{key}")
    for v in value:
        if v not in sorted_list:
            sorted_list.append(v)
            print(f"-- {v}")
    sorted_list.clear()
