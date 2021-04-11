letters = input()
index = []


for letter in range(len(letters)):
    if letters[letter].isupper():
        index.append(letter)
print(index)