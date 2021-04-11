first_line = input().split()
searched_palindrome = input()
second = [i for i in first_line if i == i[::-1]]
counter = [i for i in second if i == searched_palindrome]
print(second)
print(f'Found palindrome {counter.count(searched_palindrome)} times')