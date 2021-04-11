RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)

effort = 0
put_out_fire = []

fire_data = input().split("#")
water_amount = int(input())

for fire in fire_data:
    type_of_fire, value = fire.split(" = ")
    value = int(value)

    # Check if according to the type of fire value IS NOT valid -
    # then skip and continue to next fire data's row
    if type_of_fire == "High" and value not in RANGE_HIGH:
        continue
    elif type_of_fire == "Medium" and value not in RANGE_MEDIUM:
        continue
    elif type_of_fire == "Low" and value not in RANGE_LOW:
        continue

    # TODO check if water is enough to
    if water_amount >= value:
        water_amount -= value
        effort += value * 0.25
        put_out_fire.append(value)

#Print out data for put out fire celss

print("Cells:")
for fire_value in put_out_fire:
    print(f" - {fire_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_fire)}")