uncomfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()
    print(f"Verifying: {current_user.title()}...")
    confirmed_users.append(current_user)

print("\nConfirmed Users:")
for user in confirmed_users:
    print(f"{user.title()}")