def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


def get_formatted_name(first_name, last_name):
    """Return a neatly formatted full name"""
    fullName = f"{first_name} {last_name}"
    return fullName.title()
    

def menu_loop():
    while True:
        print('\nTell me your Name: ')
        print("(Press 'q' at any time to quit)")
        fName = input("First Name: ")
        if fName == 'q':
            break
        lName = input("Last Name: ")
        if lName == 'q':
            break

        formattedName = get_formatted_name(fName, lName)
        print(f"\nHello, {formattedName.title()}!")



menu_loop()