data = input()

index = 0
current = ""
result = ""
while index < len(data):

    if not data[index].isdigit():
        current += data[index]
        index += 1
    else:
        current_number = ""
        while data[index].isdigit():
            current_number += data[index]
            index += 1
            if index == len(data):
                break
        current_number = int(current_number)
        output = current.upper() * current_number
        result += output
        current = ""
print(f"Unique symbols used: {len(set(result))}")
print(result)