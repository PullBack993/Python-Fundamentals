import re

number = int(input())
pattern = r"\!(?P<name>[A-Z]{1}[a-z]{3,})\!:\[(?P<encrypt>[A-Za-z]{8,})\]"
encrypt_message_name = ""
encrypt_message_ord = ""
ord_print = ""
counter = 0
for n in range(number):
    data = input()
    if re.match(pattern, data):
        for m in re.finditer(pattern, data):
            encrypt_message_name = m.group('name')
            encrypt_message_ord = m.group('encrypt')
            for e in encrypt_message_ord:
                ord_print += str((ord(e)))
                counter += 1
                if len(encrypt_message_ord) <= counter:
                    pass
                else:
                    ord_print += " "
            print(f"{encrypt_message_name}: {ord_print}")
    else:
        print('The message is invalid')
