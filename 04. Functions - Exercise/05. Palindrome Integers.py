def is_palindrome(element):
    current_element = element[::-1]
    if element == current_element:
        return True
    return False

def sep_element(text, sep):
    num_str = text.split()
    return num_str


data = input()
nums_str = sep_element(data, ", ")

for el in nums_str:
    print(is_palindrome(el))
