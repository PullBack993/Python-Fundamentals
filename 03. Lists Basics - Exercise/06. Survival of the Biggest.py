list_of_numbers = [int(num) for num in input().split()]
numbers_of_removing = int(input())

for number in range(numbers_of_removing):
    list_of_numbers.remove(min(list_of_numbers))
print(list_of_numbers)