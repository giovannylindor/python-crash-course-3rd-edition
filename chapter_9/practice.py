# During Reading "Working with Classes and Instances"
# Here are my implementations of 'getters' and 'setters' 

class Player: 

    def __init__(self, username, id):
        self.username = username
        self.id = id


    # getters
    def get_username(self):
        return self.username
    
    
    def get_id(self):
        return self.id
    
    
    # setters
    def set_username(self, username):
        self.username = username
    

    def set_id(self, id):
        self.id = id



user = Player('admin', 224432124)
user.set_id(221267453)
print(f"{user.get_id()}")
print(f"\n{user.get_username()}")