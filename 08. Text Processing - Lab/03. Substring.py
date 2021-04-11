first_line = input()
second_line = input()

while first_line in second_line:
    second_line = second_line.replace(first_line, "")
print(second_line)