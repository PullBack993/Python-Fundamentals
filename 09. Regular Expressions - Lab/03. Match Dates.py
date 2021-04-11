import re
data = input()
pattern = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"

dates = re.finditer(pattern, data)
for date in dates:
    d = date.groupdict()
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")