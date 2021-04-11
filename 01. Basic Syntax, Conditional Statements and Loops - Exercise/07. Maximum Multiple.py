divisor = int(input())
bound = int(input())
largest_integer = 0

for i in range(bound+1):
    if i % divisor == 0:
        largest_integer = i
print(largest_integer)