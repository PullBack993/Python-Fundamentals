usernames = input().split(", ")

for username in usernames:
    if 3 <= len(username) <= 16:
        if username.isalpha() or username.isalnum() or "-" in username or '_' in username:
            print(username)


#sh, too_long_username, !lleg@l ch@rs, jeffbutt
#or username.isdigit() or username.isalpha() or username in '-' or username in "_":