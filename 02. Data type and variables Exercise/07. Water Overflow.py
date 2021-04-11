n = int(input())

total = 0
capacity = 255

while n > 0:
    liters = int(input())
    n -= 1
    total += liters
    if capacity < total:
        print('Insufficient capacity!')
        total -= liters

print(total)