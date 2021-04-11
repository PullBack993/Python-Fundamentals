number = int(input())
word = input()

counter_real = []
match_words = []
for n in range(number):
    n_lines = str(input())
    counter_real.append(n_lines)
    if word in n_lines:
        match_words.append(n_lines)

print(counter_real)
print(match_words)