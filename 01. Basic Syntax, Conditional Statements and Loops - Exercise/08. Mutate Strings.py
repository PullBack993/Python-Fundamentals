string_1 = input()
string_2 = input()

result_str = ''
previous_str = string_1

for i in range(len(string_1)):
    for index_2 in range(i + 1):
        result_str += string_2[index_2]

    for index_1 in range (i + 1, len(string_1)):
        result_str += string_1[index_1]

    if not previous_str == result_str:
        print(result_str)

    previous_str = result_str
    result_str = ''
