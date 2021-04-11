text = input().split()
half = len(text) // 2
first = text[:half]
second = text[:half:-1]
sum_of_first = 0
sum_of_second = 0

for n in first:
    sum_of_first += int(n)
    if n == '0':
        sum_of_first *= 0.8

for n in second:
    sum_of_second += int(n)
    if n == '0':
        sum_of_second *= 0.8

if sum_of_first == 0 or sum_of_second == 0:
    exit()
if sum_of_first > sum_of_second:
    print(f'The winner is right with total time: {sum_of_second:.1f}')
else:
    print(f'The winner is left with total time: {sum_of_first:.1f}')