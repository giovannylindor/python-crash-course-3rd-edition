responses = {}
polling_active = True

while polling_active:
    name = input("\nName: ")
    response = input("Mountain: ")
    responses[name] = response
    repeat = input('Another Response? \nYes/No: ')
    
    if repeat == 'no':
        polling_active = False


print(f"\n\n{responses}")

print("\nPoll Results:")
for name, response in responses.items():
    print(f"{name.title()} wants to climb {response.title()}")