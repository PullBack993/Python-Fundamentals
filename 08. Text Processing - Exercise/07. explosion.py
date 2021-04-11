text = input().split(">")
explode = 0
after_explode = []
for index_text in text:
    if index_text[0].isdigit():
        explode += int(index_text[0])
        if len(index_text) <= explode:
            explode -= len(index_text)
            index_text = '>'
        else:
            index_text = '>' + "".join(list(index_text[explode::]))
            explode = 0
    after_explode.append(index_text)
print("".join(after_explode))