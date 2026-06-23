class Dog:
    """Modeling a Dog."""

    def __init__(self, name, age):
        """Initialize name and age"""
        self.name = name
        self.age = age

    
    def sit(self):
        """Dog sitting"""
        print(f"{self.name.title()} is now sitting.")
    
    
    def roll_over(self):
        """Dog rolling over"""
        print(f"{self.name.title()} has rolled over!")


my_dog = Dog('Willie', 6)
new_dog = Dog(age=9, name='Carlos')

print(f"My Dog's name is {my_dog.name}"
      f"\nMy Dog is {my_dog.age} years old.")

new_dog.roll_over()