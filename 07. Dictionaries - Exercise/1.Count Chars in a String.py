chars = input()
out_put = {}

for char in range(len(chars)):
    key = chars[char]
    if chars[char] == ' ':
        continue
    if chars[char] not in out_put:
        out_put[chars[char]] = 1
    else:
        out_put[chars[char]] += 1
for key, value in out_put.items():
    print(f'{key} -> {value}')