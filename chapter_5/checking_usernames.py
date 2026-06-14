current_users = ['nineninesixteensixteen', 'gi3vnny', 'brickscamecheap', 'thaddaholics', 'BallinGee']
new_users = ['johndoe', 'realpopsmoke', 'BallinGee', 'kingjames', 'gi3vnny']

for user in range(len(current_users)):
    current_users[user] = current_users[user].lower()


for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user.lower()} is not available")
    else:
        print(f"{new_user.lower()} is available!")