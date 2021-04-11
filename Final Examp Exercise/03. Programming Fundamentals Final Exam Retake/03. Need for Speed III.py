from collections import defaultdict
number_of_cars = int(input())

cars = defaultdict(dict)
for n in range(number_of_cars):
    data = input()
    car, mileage, fuel = data.split("|")
    cars[car]['mileage'] = int(mileage)
    cars[car]['fuel'] = int(fuel)

command = input()

while not command == "Stop":
    name_command = command.split(" : ")
    if name_command[0] == 'Drive':
        car = name_command[1]
        distance = name_command[2]
        fuel = name_command[3]
        enough_fuel = cars[car]['fuel'] - int(fuel)
        if enough_fuel <= 0:
            print(f"Not enough fuel to make that ride")
        elif enough_fuel > 0:
            cars[car]['fuel'] -= int(fuel)
            cars[car]['mileage'] += int(distance)
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]['mileage'] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
    elif name_command[0] == 'Refuel':
        car = name_command[1]
        fuel = name_command[2]
        fuel = int(fuel)
        total_fuel = cars[car]['fuel'] + fuel
        if total_fuel >= 75:
            difference = 75 - cars[car]['fuel']
            cars[car]['fuel'] = 75
            print(f"{car} refueled with {difference} liters")
        else:
            cars[car]['fuel'] = total_fuel
            print(f"{car} refueled with {fuel} liters")
    elif name_command[0] == 'Revert':
        car = name_command[1]
        kilometers = name_command[2]
        kilometers = int(kilometers)
        difference = cars[car]['mileage'] - kilometers
        if difference < 10000 and cars[car]['mileage'] >= 10000:
            cars[car]['mileage'] = 10000
            command = input()
            continue
        else:
            cars[car]['mileage'] = cars[car]['mileage'] - kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")
                                                                            
    command = input()

sorted_cars = sorted(cars.items(), key=lambda tkvp: (-tkvp[1]['mileage'], tkvp[0]))

for car, value in sorted_cars:
    print(f"{car} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")