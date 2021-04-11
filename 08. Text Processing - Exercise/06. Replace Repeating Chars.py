import re
data = input()
a = re.sub(r'(.)\1+', r'\1', data)
print(a)