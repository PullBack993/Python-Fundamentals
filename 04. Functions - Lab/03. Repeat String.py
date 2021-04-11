repeating_word = input()
repeated_times = int(input())

def repeating_string(word, n_times):
    result = word * n_times
    return result


print(repeating_string(repeating_word, repeated_times))
