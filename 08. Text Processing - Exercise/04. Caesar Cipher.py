data = input()
encrypted_version = ''
for i in data:
    encrypted_version += (chr(ord(i) - 3))
print(encrypted_version)
