import re
data = input()
pattern = r"\d+"
end_printing = []

while data:
    match = re.findall(pattern, data)
    if match:
        end_printing.extend(match)
    data = input()
print(" ".join(end_printing))