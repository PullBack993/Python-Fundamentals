data = input()
digits = ""
letters = ""
other = ""

for chr in data:
    if chr.isdigit():
        digits += chr
    elif chr.isalpha():
        letters += chr
    else:
        other += chr
print(digits)
print(letters)
print(other)