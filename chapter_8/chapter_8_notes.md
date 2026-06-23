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

##### Preventing a Function from Modifying a List
Using the _slice notation_ makes a copy of a list to send into a function
It does not affect the original list 
`function_name(list_name[:])`

- - -

##### Passing an Arbitrary Number of Arguments

Python allows a function to collect an arbitrary number of arguments from the calling statement 
See `pizza.py`

To have a func collect an arbitrary number of args, paste `*` before the parameter

_Example_

```Python
def make_pizza(*toppings):
    """Print a list of toppings"""
    print(toppings)
```

* The asterisk tells python to make a tuple containing all the values the function will receive 
    - This syntax works with no matter how many args a function will receive

- - -

##### Mixing Positional and Arbitrary Arguments

If you want a func to accept several kinds of args, the param that accepts arbitrary args, **MUST BE PLACED LAST in the DEF**

See `pizza.py`
_Example_

`def make_pizza2(size, *toppings):`

_NOTE_: You'll often see a parameter name `*args` which collects arbitrary positional args

- - - 

##### Using Arbitrary Keyword Arguments

Sometimes you'll accept arbitrary keyword args, but won't know ahead of time the info passed to a function. 

You can write functions that accept K-V pairs 
See `user_profile.py`

```Python
def build_profile(first, last, **user_info):
    """Build a Dictionary containing user information"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info
```

* The `**` Tells Python to create a dictionary containing arbitrary key-value pairs

* You can mix positional, keyword, and arbitrary values in different ways when writing your own functions 

_NOTE_: You'll often see a parameter name `**kargs` which collects nonspecific (k-v) keyword args

- - - 

##### Storing your functions in Modules

Functions separate blocks of code from your main program
You can store your functions in a separate file called _modules_, then import it into your main program 

- An `import` statement tells python to make the code in a module available in the runnning program file.


* Storing functions in a seperate file allows you to hide the details of your program code and focus on higher-level logic
- It allows you to reuse functions in different programs
- You can share those files w/ other programmers w/o having to share your entire program

**Importing an entire module**

1. Create a module
- A module is a file that ends w/ `.py` which contains code you want to import
_Example_ &rarr; take the `pizza.py` file in the `./modules` folder

`pizza.py`
```Python
def makePizza(size, *toppings):
    print(f"Making a {size}-inch pizza w/ the following: ")
    for topping in toppings:
        print(f"- {topping.title()}")
```

2. Make a seperate file in the same directory then import it
_Example_ &rarr; create `making_pizzas.py` then import `pizza.py`

`making_pizzas.py`
```Python
import pizza

pizza.makePizza(16, 'pepperoni', 'sausage', 'extra cheese')
print()
pizza.makePizza(16, 'pepperoni')
```

* `import pizza` tells python to open `pizza.py` and copy all the functions 
<br>

* To call a function from an imported module, enter the name of the module, followed by the `.functionName()`

- - - 

**Importing Specific Functions**

Syntax for importing a specific function from a module 

`from module_name import function_name`

* You can import as many functions as you want from a module, by sepearating each functions name w/ a comma

_Ex_: `from module_name import function_0, function_1, function_2`

* See `making_pizzas2.py`
`from pizza import makePizza`

**_NOTE_**: You don't need to use dot notation because the function is explicitly imported

- - - 

**Using `as` to Give a Function an Alias**

If the name of an imported function might conflict w/ another name,
using an alias will relieve conflicts 

_Example_: `from module_name import function_name as alias`

* See `making_pizzas3.py`
`from pizza import makePizza as mp`

- - - 

**Using `as to give a Module an Alias**

You can use `as` to provide an alias for a module name
Doing this allows you to call functions more quickly

* See `making_pizzas4.py` 
`import pizza as p`

- - - 

**Importing all functions in a Module**

You can tell Python to import every function in a module by using the `*` operator

The `*` in the import tells Pyton to copy every function from a module into your current program 
* Because of this, you can call each function by name w/o dot notation

See `player.py` and `making_player.py`

**_NOTE_**: It's not best to use this approach when working w/ large modules you didn't write 

**BEST APPROACH**: 
* Import functions you want
* Import entire module + use dot notation 

This leads to clear code thats easy to read

- - - 

##### Styling Functions 

* Functions should have **_Descriptive Names_**
    - Should include lowercase letters & underscores
    - They help you and others understand what your code is trying to do

* Every function should have a comment explaining what it does
    - Use """""" Format
    - Should appear after func def

* If you specify a default val, no spaces should be used on either side of the `=` sign
    - `def function_name(param0, param1='def')`
    Same w/ keyword args 
    - `function_name(value0, param1='val')`


* Limit lines to 79 chars 

* If your program/module has more than 1 func, separate each by 2 blank lines to 
make it easier to read

* All `import`'s should be written at the beginning of a file