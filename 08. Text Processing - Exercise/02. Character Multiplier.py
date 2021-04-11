character = input().split()
result = 0
most_long = 0
first, second = character
if len(character[0]) > len(character[1]):
    most_long = len(character[0])
elif len(character[1]) > len(character[0]):
    most_long = len(character[1])
else:
    most_long = len(character[0])

for ch in range(most_long):
    if ch > len(first)-1 and len(first) < len(second):
        result += ord(second[ch])
    elif ch > len(second)-1 and len(second) < len(first):
        result += ord(first[ch])
    else:
        result += ord(first[ch]) * ord(second[ch])
print(result)
