a = int(input())
b = int(input())
c = int(input())
def smallest_of_number(a, b, c):
    smallest_number = 0
    if a <= b and a < c:
        smallest_number = a
    elif b <= a and b <= c:
        smallest_number = b
    else:
        smallest_number = c
    return smallest_number


print(smallest_of_number(a, b, c))