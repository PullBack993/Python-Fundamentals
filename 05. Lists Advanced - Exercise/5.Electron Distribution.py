number = int(input())

shell = []
max_electrons = 0
n = 1

while number > 0:
    max_electrons = 2 * n ** 2
    if max_electrons > number:
        shell.append(number)
    else:
        shell.append(max_electrons)
    number -= max_electrons
    n += 1

else:
    print(shell)