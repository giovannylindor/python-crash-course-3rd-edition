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