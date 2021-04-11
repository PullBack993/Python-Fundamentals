substrings_list = input().split(', ')
words_list = input().split(', ')

unique_substrings = [subst for subst in substrings_list for words in words_list if subst in words]
print(sorted(set(unique_substrings), key=unique_substrings.index))
