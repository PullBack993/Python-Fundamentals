number = float(input())

while not (number <= 100 and number >= 1):
    #while 100 < number < 1:
    number = float(input())
print(f'The number {number} is between 1 and 100')

#or

while True:
    number = float(input())
    if 100 < number < 1:
        break