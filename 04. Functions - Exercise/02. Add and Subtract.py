n1 = int(input())
n2 = int(input())
n3 = int(input())

def sum_number(num1, num2, num3):
    sum_of_a_b = num1 + num2
    subst_sum_c = sum_of_a_b - num3
    return subst_sum_c


print(sum_number(n1, n2, n3))