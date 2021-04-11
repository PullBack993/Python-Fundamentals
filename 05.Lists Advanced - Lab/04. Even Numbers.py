numbers = input().split(', ')
num = list(map(int, numbers))
index_of_even_numbers = [i for i in range(len(numbers)) if num[i] % 2 == 0]

print(index_of_even_numbers)
