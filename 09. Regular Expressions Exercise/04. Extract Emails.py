# (^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z])+
import re

text = input()
pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z]+\-?[a-zA-Z]+(\.[a-zA-Z]+\-?[a-zA-Z])+"

regex = [el.group() for el in re.finditer(pattern, text)]

print("\n".join(regex))