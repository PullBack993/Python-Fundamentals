import re
text = input()
pattern = r"(?P<surround>#|@)(?P<text>[A-Za-z]{3,})(?P=surround){2}(?P<text2>[A-Za-z]{3,})(?P=surround)"
pair_words = []
mirror_words = []

for txt in re.finditer(pattern, text):
    pair_words.append(txt.group())
    if txt.group('text') == txt.group('text2')[::-1]:
        mirror_words.append(f"{txt.group('text')} <=> {txt.group('text2')}")

if not pair_words:
    print("No word pairs found!")
else:
    print(f"{len(pair_words)} word pairs found!")

if not mirror_words:
    print("No mirror words!")
else:
    print(f"The mirror words are:\n{', '.join(mirror_words)}")
