factor = int(input())
count = int(input())

multiples_elements = []

for length in range(1, count+1):
    result = length * factor
    multiples_elements.append(result)
print(multiples_elements)