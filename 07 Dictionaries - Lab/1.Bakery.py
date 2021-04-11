data = input().split()
bakery = {}
for word in range(0, len(data), 2):
    key = data[word]
    value = data[word + 1]
    bakery[key] = int(value)
print(bakery)