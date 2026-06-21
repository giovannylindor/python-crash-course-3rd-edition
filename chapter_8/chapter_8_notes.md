# Chapter 8: Functions
- - - 

- To declare a function, you must begin with the word `def` to tell Python you're
defining a function

_Function Definition_ &rarr; tells Python the name and information the function needs in order to run

**_Docstring_** &rarr; Text that describes what a function does
- When python generates documentaion for functions, it looks for a string after the functions definition 
- they are enclosed in triple quotes

**Parameter** &rarr; the variable inside a function definition, the info needed for the function to do its job 

**Argument** &rarr; The specific defined information passed from a function call to a function

_Note_: Arguments and Parameters are used interchangeably 

**_Positional Arguments_**: Args that need to be in the same order the params are written

**_Keyword Arguments_**: Each arg consists of a var name and value


- - -

##### Positional Arguments

When you call a function, python must match each arg w/ a parameter in the definition.
The simplest way to do that is to do this based on the order of args provided
see `pets.py`

* **Make sure the order of the arguments in your function matches the order of params in the function definition!!!**

```Python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


# Hamster is assigned to animal_type
# Harry is assigned to pet_name
describe_pet('Hamster', 'Harry')

# NOTE: Doing describe_pet('Harry', 'Hamster') will result in the following:
# I have a Harry
# My Harry's name is Hamster

# SEE Keyword Arguments to Counteract this error from happening
```
- - -


##### Keyword Arguments 

A _keyword argument_ is a name-value pair that you pass to a function. 
You directly associate the name and the value within the argument so when you pass the argument to the function, theres no confusion

Keyword arguments free you from worrying about correctly ordering your arguments in the function call

See `pets.py`
```Python
describe_pet(animal_type='Cheetah', pet_name='Cyclops The Destroyer')
describe_pet(pet_name="Carlos", animal_type='Dog')
```

**When you use keyword args, make sure the exact names of the parameters are in the functions definition

- - - 

##### Default Values 

When writing functions you can define a defualt value for each parameter
If an arg for a param is provided, python will use that, if not, python will use a default val

Using default vals can simplify function calls and clarify how your functions are used

NOTE: If you define a function that accepts and uses args (no def arg), then call that function w/ no args, an error will arise. ' **`TRACEBACK ERROR`**

See `pets.py`
```Python
def desc_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")    
    print(f"My {animal_type.title()}'s name is {pet_name.title()}")

desc_pet(pet_name='Willie')
```

_NOTE_ when you use def vals, any param w/ a def val needs to be listed AFTER all the params that don't have def vals

- - - 

##### Equivalent Function Calls
Because positional arguments, keyword arguments, and defaults can all be used together, 
you have many ways to call a function

_Example_

```Python
def desc_pet(petName, animalType='Dog')
```

Valid Calls

```Python
dec_pet('Wille')
dec_pet(petName='Willie')

dec_pet('Wille', 'Hamster')
dec_pet(petName='Willie', animalType='Hamster')
dec_pet(animalType='Hamster', petName='Willie')
```
As long as you function calls produce the output you want, use the style you find easiest to understand

- - - 

**Avoiding Argument Errors**

* Unmatched Arguments: When you provide fewer or more arguments than a function needs to do its work (`Trackback Error`)

- - - 

##### Return Values 

*  The value the function returns is called a return value. The return statement takes a value from inside a function and sends it back to the line that called the function.

**Optional Arguments**
See `formatted_name.py`
```Python
def get_full_name(firstName, lastName, middleName=''):
    
    if middleName:
        fullName = f"{firstName} {middleName} {lastName}"
    else:
        fullName = f"{firstName} {lastName}"

    return fullName.title()
```

- - - 

##### Returning a Dictionary
See `person.py`
```Python
def build_person(firstName, lastName, age=None): 
    person = {'first': firstName, 'last': lastName}
    
    if age:
        person['age'] = age

    return person
```

- - - 

##### Using a Function w/ a While Loop
See `greeter.py`
 
- - -

##### Passing a List 
See `greet_users.py`
Similar to passing an array to a function
 
```Python
def greet_users(names):
    """Print a greeting to each user in the list"""
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)


usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

- - -

##### Modifying a List in a Function
See `printing_models.py`

_NOTE_: If you’re writing a function and notice the function is doing too many different tasks, try to split the code into two functions. Remember that you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.

- - -

