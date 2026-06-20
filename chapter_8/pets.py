def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Hamster is assigned to animal_type
# Harry is assigned to pet_name
describe_pet('Hamster', 'Harry')
describe_pet('Chimp', 'Mark')
describe_pet('Cat', 'Lorie')


# KEYWORD ARGUMENTS 
describe_pet(animal_type='Cheetah', pet_name='Cyclops The Destroyer')
describe_pet(pet_name="Carlos", animal_type='Dog')


# DEFAULT VALS
def desc_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")    
    print(f"My {animal_type.title()}'s name is {pet_name.title()}")


print()
print()
print("DEF VAL")
desc_pet(pet_name='Willie')