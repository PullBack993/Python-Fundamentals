data = input().split()
bakery = {}
for word in range(0, len(data), 2):
    key = data[word]
    value = data[word + 1]
    bakery[key] = int(value)

search_product = input().split()
for product in search_product:
    if product in bakery:
        print(f'We have {bakery[product]} of {product} left')
    else:
        print(f"Sorry, we don't have {product}")