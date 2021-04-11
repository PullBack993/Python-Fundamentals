all_cells = input().split('#')
water = int(input())
effort = 0
fire = 0
cells_value = []

for cell in all_cells:
    current_cell = cell.split(' = ')
    type_of_fire = current_cell[0]
    cell_value = int(current_cell[-1])
    if type_of_fire == 'High':
        if not 81 <= cell_value <= 125:
            continue
    elif type_of_fire == "Medium":
        if not 51 <= cell_value <= 80:
            continue
    elif type_of_fire == "Low":
        if not 1 <= cell_value <= 50:
            continue
    if water < cell_value:
        continue
    cells_value.append(cell_value)
    water -= cell_value
    effort += cell_value * 0.25
    fire += cell_value

print('Cells:')
for cell in cells_value:
    print(f' - {cell}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {fire}')