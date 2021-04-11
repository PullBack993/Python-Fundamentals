# www\.[a-zA-z0-9]+[\-]?[a-zA-z0-9]+(\.[a-zA-Z]+[a-zA-Z])+
import re
text = input()
patter = r"(^|(?<=\s))www\.[A-Za-z0-9-]+(\.[a-z]+)+($|(?=\s))"
while text:
    for el in re.finditer(patter, text):
        print(el.group())
    text = input()