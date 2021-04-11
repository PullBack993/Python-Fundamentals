import re
sentence = input()
word = input()

pattern = f"\\b{word}\\b"
result = re.findall(pattern, sentence, re.IGNORECASE)
print(len(result))