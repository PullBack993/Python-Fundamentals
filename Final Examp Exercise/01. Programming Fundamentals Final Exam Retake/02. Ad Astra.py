import re

data = input()

pattern = r"(#|\|)(?P<name>[A-Za-z\s]+)\1(?P<data>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<calories>([0-9][0-9]{0,3})|10000)\1"
total_calories = 0
for index in re.finditer(pattern, data):
    total_calories += int(index.group('calories'))

print(f"You have food to last you for: {total_calories // 2000} days!")
for m in re.finditer(pattern, data):
    print(f"Item: {m['name']}, Best before: {m['data']}, Nutrition: {m['calories']}")