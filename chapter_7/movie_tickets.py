prompt = 'Enter your age: '
people = 0

while True:
    message = input(prompt)    
    
    if message.lower() == 'quit':
        break

    if not message.isdigit():
        print("Please enter a valid number!")
        continue

    age = int(message)

    if age < 3:
        people += 1
        print("Price: Free")
    elif age <= 12:
        people += 1
        print("Price: $10")
    else:
        people += 1
        print("Price: $15")
    

if people == 0:
    exit()
else: 
    print(f"There are a total of {people} people who want Movie Tickets.")
