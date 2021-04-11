text = input()
emoji = [f"{text[x]}{text[x+1]}" for x in range(0, len(text)) if text[x] == ':']
print("\n".join(emoji))