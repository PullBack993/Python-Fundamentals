text = input()
word = []
number = []
take = []
skip = []
rope = []
for t in text:
    if t.isdigit():
        number.append(int(t))
    else:
        word.append(t)

for n in range(len(number)):
    if n % 2 == 0:
        take.append(number[n])
        take_element = word[:number[n]]
        rope.append(take_element)
        del word[:number[n]]
    else:
        skip.append(number[n])
        skip_element = word[:number[n]]
        del word[:number[n]]

for x in rope:
    if not x == '[]':
        print("".join(x), end='')