numbers = int(input())

n = []
filtered = []

for i in range(numbers):
    current_number = int(input())
    n.append(current_number)

command = input()

if command == 'even':
    for number in n:
        if number % 2 == 0:
            filtered.append(number)

elif command == 'odd':
    for number in n:
        if number % 2 != 0:
            filtered.append(number)

elif command == 'negative':
    for number in n:
        if number < 0:
            filtered.append(number)

elif command == 'positive':
    for number in n:
        if number >= 0:
            filtered.append(number)

print(filtered)
