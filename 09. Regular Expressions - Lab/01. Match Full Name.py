import re
data = input()
pattern = r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b"

name = re.findall(pattern, data)
print(" ".join(name))
