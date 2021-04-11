product = input()
quantity = float(input())


def orders(current_product, current_quantity):
    result = None
    if current_product == 'coffee':
        result = current_quantity * 1.50
    elif current_product == 'water':
        result = current_quantity * 1.00
    elif current_product == 'coke':
        result = current_quantity * 1.40
    elif current_product == 'snacks':
        result = current_quantity * 2.00
    return result


print(f'{orders(product, quantity):.2f}')
