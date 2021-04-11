command = input()
coast = 0
tax = 0
total = 0
while not command == "special" and not command == "regular":
    command = float(command)
    if command < 0:
        print("Invalid price!")
        command = input()
        continue
    coast += command
    command = input()
if coast == 0:
    print("Invalid order!")
    exit()
if command == 'special':
    tax = coast * 20 / 100
    total = (coast + tax) * 0.9
    if total == 0:
        print("Invalid order!")
    print(f"Congratulations you've just bought a new computer!"
          f"\n Price without taxes: {coast:.2f}$"
          f"\nTaxes: {(coast * 20/ 100):.2f}$\n-----------\nTotal price: {total:.2f}$")
else:
    total = coast + tax
    if total == 0:
        print("Invalid order!")
    print(f"Congratulations you've just bought a new computer!"
          f"\n Price without taxes: {coast:.2f}$\nTaxes: {(coast * 20/ 100):.2f}$"
          f"\n-----------\nTotal price: {total+ (coast * 20 / 100):.2f}$")