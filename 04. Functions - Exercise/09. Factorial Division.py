def cal_factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num

    return result


number_1 = int(input())
number_2 = int(input())
factorial_n = cal_factorial(number_1)
factorial_2 = cal_factorial(number_2)

end_result = factorial_n / factorial_2
print(f'{end_result:.2f}')