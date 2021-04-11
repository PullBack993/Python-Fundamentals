numbers = [int(n) for n in input().split(', ')]
for n in numbers:
    if n == 0:
        numbers.remove(n)
        numbers.append(0)
print(numbers)