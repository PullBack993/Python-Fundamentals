name = input()
my_dict = {}
while not name == 'statistics':
    product_name, quantity = name.split(": ")
    quantity = int(quantity)
    if product_name not in my_dict:
        my_dict[product_name] = quantity
    else:
        my_dict[product_name] += quantity
    name = input()

print('Products in stock:')
for key, value in my_dict.items():
    print(f'- {key}: {value}')
print(f'Total Products: {len(my_dict)}')
print(f"Total Quantity: {sum(my_dict.values())}")