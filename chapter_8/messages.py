short_messages = ['Hello, World!', 'Goodbye World!', 'Sleep!!!', 'Goodbye!']

def show_messages(arr): 
    for message in arr:
        print(f"{message}")



new_messages = []

def send_messages(arr, new_arr):
    while arr: 
        curr = arr.pop()
        print(f"{curr}")
        new_arr.append(curr)


send_messages(short_messages[:], new_messages)
print(f"\n{short_messages}\n{new_messages}")