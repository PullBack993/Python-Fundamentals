def perfect_num(num):
    proper_divisors = []

    for n in range(1, num):
        if num % n == 0:
            proper_divisors.append(n)

    if sum(proper_divisors) == num:
        return True
    return False


n = int(input())

if perfect_num(n):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")