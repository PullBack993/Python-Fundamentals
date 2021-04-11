import re
data = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

dates = re.finditer(pattern, data)
for d in dates:
    print(d.group(0), end=" ")