class User: 

    def __init__(self, first_name, last_name, username):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.username = username
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"First Name: {self.first_name}"
              f"\nLast Name: {self.last_name}"
              f"\nUsername: {self.username}")


    def greet_user(self):
        print(f"Hello, {self.username}!")


    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privilages = Privileges()


class Privileges():
    def __init__(self):
        self.privilages = ['can add post', 'can delete post', 'can ban user']

    def show_privilages(self):
        print(f"Privilages: ")
            
        for privilage in self.privilages:
            print(f"{privilage.capitalize()}")



new_admin = Admin('Giovanny', 'Lindor', 'gi3vnny')
new_admin.privilages.show_privilages()
