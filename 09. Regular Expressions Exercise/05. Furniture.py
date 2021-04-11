import re
line = input()
pattern = r"(^>>)(?P<name>\w+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)($|\s)"
result = []
total_price = 0
while not line == 'Purchase':
    match = re.match(pattern, line)
    if match:
        obj = match.groupdict()
        result.append(obj["name"])
        total_price += float(obj["price"]) * int(obj['quantity'])
    line = input()

print("Bought furniture:")
for name in result:
    print(name)
print(f"Total money spend: {total_price:.2f}")