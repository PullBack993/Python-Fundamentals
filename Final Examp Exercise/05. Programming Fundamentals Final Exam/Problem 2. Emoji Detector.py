import re
text = input()
patter_for_emoji = r"(::[A-Z][a-z]{2,}::)|(\*\*[A-Z][a-z]{2,}\*\*)"
patter_for_cool = r"\d"
number = 0
list_with_emoji = []
emoji_value = 0
num_cool_threshold = 1
for index in re.finditer(patter_for_cool, text):
    for i in index.group():
        num_cool_threshold *= int(i)
print(f"Cool threshold: {num_cool_threshold}")
for e in re.finditer(patter_for_emoji, text):
    list_with_emoji.append(e.group())
print(f"{len(list_with_emoji)} emojis found in the text. The cool ones are: ")
for emoji in list_with_emoji:

    for c in emoji:
        if c.isalpha():
            emoji_value += ord(c)
    if emoji_value >= num_cool_threshold:
        print(emoji)
        emoji_value = 0
    else:
        emoji_value = 0