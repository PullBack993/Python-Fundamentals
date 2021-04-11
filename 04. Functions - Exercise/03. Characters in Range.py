index_1 = input()
index_2 = input()

def char_in_range(begin, end):
    convert_1 = ord(begin)
    convert_2 = ord(end)
    result = []
    for i in range(convert_1+1, convert_2):
        result.append(chr(i))
    return print(*result, end=' ')


char_in_range(index_1, index_2)