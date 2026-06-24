class Privileges():
    def __init__(self):
        self.privilages = ['can add post', 'can delete post', 'can ban user']

    def show_privilages(self):
        print(f"Privilages: ")
            
        for privilage in self.privilages:
            print(f"{privilage.capitalize()}")