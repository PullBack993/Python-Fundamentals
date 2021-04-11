lines = int(input())
total = 0
while lines > 0 :
    letters = input()
    lines -= 1
    total += ord(letters)
print(f'The sum equals: {total}')