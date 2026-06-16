prompt = '\nSay Something: '
prompt += "\nEnter \"Quit\" to End"
prompt += "\nPrompt: "
message = ""

while message.lower() != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)