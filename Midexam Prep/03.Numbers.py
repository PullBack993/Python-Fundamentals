numbers = [int(n) for n in input().split()]
average = sum(numbers) // len(numbers)
top_5 = []
for n in numbers:
    if n > average:
        top_5.append(int(n))

if len(top_5) > 1:
    a = list(reversed(sorted(top_5)))
    print(*a[:5])
else:
    print(f'No')