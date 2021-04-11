number = input()
result_even = 0
result_odd = 0

for i in number:
    i = int(i)
    if i % 2 == 0:
        result_even += i
    else:
        result_odd += i
print(f'Odd sum = {result_odd}, Even sum = {result_even}')
