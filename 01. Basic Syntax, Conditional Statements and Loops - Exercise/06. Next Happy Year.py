# year = int(input())
# year += 1
# while True:
#     if len(set(str(year))) == len(str(year)):
#         print(year)
#         break
#     print(len(set(str(year))))
#     print(len(str(year)))

year = int(input())+1
while True:
    year_str = str(year)
    is_happy = True

    for i in range(len(year_str)):

        for a in range(len(year_str)):
            if i == a:
                continue
            elif year_str[i] == year_str[a]:
                is_happy = False
                break

    if is_happy:
        print(year)
        break
    else:
        year += 1