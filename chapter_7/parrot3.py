prompt = 'Enter Text: '
active = True


while active: 
    message = input(prompt)
    if message.lower() == 'quit':
        active = False
    else: 
        print(f"Text: {message}")