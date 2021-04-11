def check_password_is_valid(password):
    is_valid = True
    count_digits = 0

    if len(password) < 6 or len(password) > 10:
        print('Password must be between 6 and 10 characters')
        is_valid = False

    for el in password:
        if el.isdigit():
            count_digits += 1

    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    if count_digits < 2:
        is_valid = False
        print('Password must have at least 2 digits')

    return is_valid


password = input()
result = check_password_is_valid(password)

if result:
    print('Password is valid')