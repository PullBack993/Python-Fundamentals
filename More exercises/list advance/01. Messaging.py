numbers = input().split()
text = input()

word = ''

for num in numbers:
    sum_numbers = sum(int(num) for num in num)

    while sum_numbers >= len(text):
        sum_numbers -= len(text)

    word += text[sum_numbers]
    text = text[:sum_numbers] + text[sum_numbers + 1:]

print(word)