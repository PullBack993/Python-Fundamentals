text = input()
result = ""
strength = 0

for char in range(len(text)):
    char_in_text = text[char]
    if char_in_text == ">":
        strength += int(text[char+1])
        result += char_in_text
    elif not strength == 0:
        strength -= 1
    else:
        result += char_in_text
print(result)