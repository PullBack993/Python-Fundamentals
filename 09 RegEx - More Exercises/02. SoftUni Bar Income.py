# import re
# data = input()
# pattern = r"%(?P<customer>([A-Z]{1}[a-z]+))%|<(?P<product>[\w]+)>|\|(?P<counter>[\d]+)|\||(?P<price>([\d]+(\.[\d]+)?))\$"
#
# total = 0
#
# while not data == 'end of shift':
#     for m in re.finditer(pattern,data):
#         total_price = int(m.group('counter')) * float(m.group('price'))
#         print(f"{m.group('customer')}: {m.group('product')} - {total_price:.2f}")
#         total += total_price
#         data = input()
# print(f'Total income: {total:.2f}')

import re

data = input()
cust = r'(?<=\%)([A-Z][a-z]+)(?=\%)'
prod = r'(?<=\<)([\w]+)(?=\>)'
quantity = r'(?<=\|)([\d]+)(?=\|)'
prc = r'([\d]+(\.[\d]+)?)(?=\$)'
income = 0
while not data == 'end of shift':
    match_cust = re.search(cust, data)
    match_prod = re.search(prod, data)
    match_count = re.search(quantity, data)
    match_price = re.search(prc, data)
    if match_cust and match_prod and match_count and match_price:
        customer = match_cust.group()
        product = match_prod.group()
        count = int(match_count.group())
        price = float(match_price.group())
        total = count * price
        print(f'{customer}: {product} - {total:.2f}')
        income += total

    data = input()

print(f'Total income: {income:.2f}')