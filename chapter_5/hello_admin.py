usernames = ['gi3vnny', 'thaddaholics', 'javier.soul', 'realfcp', 'rostackss', 'nogramm.ja', 'admin']

for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}")

# 5-9

usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}")
else:
    print("We need some users")
