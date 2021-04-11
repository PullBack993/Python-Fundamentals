def exchange(nums_list, index):
    if 0 <= index < len(nums):
        first_part = nums_list[index + 1:]
        second_part = nums_list[:index + 1]
        result = first_part + second_part
        return result
    print("Invalid index")
    return nums


def find_max_min_num(num_list, odd_or_even):
    filtered_nums = []
    if odd_or_even == 'odd':
        for el in num_list:
            if not el % 2 == 0:
                filtered_nums.append(el)
    else:
        for el in num_list:
            if el % 2 == 0:
                filtered_nums.append(el)

    if not filtered_nums:
        return 'No matches'
    if command == 'max':
        max_element = max(filtered_nums)
        index = len(num_list) - num_list[::-1].index(max_element) - 1
        return index
    else:
        min_element = min(filtered_nums)
        index = len(num_list) - num_list[::-1].index(min_element) - 1
        return index


def element_even_odd(element, count, even_odd):
    element_filt = []
    if len(nums) < count >= 0:
        return 'Invalid count'

    if even_odd == 'odd':
        for current_element in element:
            if not current_element % 2 == 0:
                element_filt.append(current_element)
    else:
        for current_element in element:
            if current_element % 2 == 0:
                element_filt.append(current_element)
    if command == 'first':
        return element_filt[:count]
    else:
        return element_filt[:count:]


num_as_string = input().split()
nums = []

for el in num_as_string:
    nums.append(int(el))

command_data = input().split()

while not command_data[0] == 'end':
    command = command_data[0]
    if command == 'exchange':
        i = int(command_data[1])
        nums = exchange(nums, i)

    elif command == 'max' or command == 'min':
        odd_or_event = command_data[1]
        print(find_max_min_num(nums, odd_or_event))

    elif command == 'first' or command == 'last':
        list_element = nums
        count = int(command_data[1])
        even_odd = command_data[2]
        print(element_even_odd(list_element, count, even_odd))

    command_data = input().split()

print(nums)