operator = input()
first_number = int(input())
second_number = int(input())

def calculation(first, second, current_operator):
    result = None
    if current_operator == 'multiply':
        result = first_number * second_number
    elif current_operator == 'divide':
        result = first_number // second_number
    elif current_operator == 'add':
        result = first_number + second_number
    elif current_operator == 'subtract':
        result = first_number - second_number
    return result


print(calculation(first_number, second_number, operator))