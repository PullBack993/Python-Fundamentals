data = input().split()
new_dict = {}

for word in data:
    lower_word = word.lower()
    if lower_word not in new_dict:
        new_dict[lower_word] = 0
    new_dict[lower_word] += 1

for key, value in new_dict.items():
    if value % 2 == 1:
        print(key, end=' ')