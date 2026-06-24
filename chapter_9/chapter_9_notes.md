# Chapter 9: Classes 
- - - 

* Class = Blueprint
* Object = Instance of the Blueprint

An object from a class is called an _instance_.


- - -

**Creating & Using a Class**
`dog.py`
```Python
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
```
- - - 

##### `__init__()` Method

* A function that's apart of a class is called a _method_. 

* The `__init__()` method runs automatically whenever a new instance is created
    - It is in essence similar to a constructor
    - `self` is a param requried in the method def and it must come first
    -  `self` is needed because method call will auto pass the `self` arg

- - - 

**`self`**

Every method call associated w/ an instance will automatically call `self`

`self` is a reference to the instance itself
- it gives an instance access to a classes attributes and methods

* Any var prefixed w/ self is available to every method in the class
    - it will be able to access these vars through any intance 


* When we make an instance of `Dog` Python calls `__init__()`
    - You pass a name and age (`self` is not needed to be passed as its called automatically)


* Variables that are accessible through instances are called _attributes_

* `self` does not need to be included as an argument!!!

- - -

**Making an Instance**

`dog.py`
```Python
my_dog = Dog('Willie', 6)
```

* Python calls `__init__()` and sets `self.name` to Willie and `self.age` to 6
    - the args are positional
    - you can use keyword args as well!

- - -


_NOTE_: Defining a Class name w/ a Capital Letter is a proper naming convention

**Accessing Attributes**

To access attributes you use dot notation 
- _instance_._attribute_

_Example_ 
* To access a dogs name 
    - `my_dog.name`
       
- - - 

**Calling Methods**

To access/call a method: 
- _instanceName_._method()_

```Python
new_dog.roll_over()
```

- - - 

##### Working with Classes and Instances

* Once you create a class, you'll spend most of your time working w/ instances created from that class 
    - One of the first tasks you'll do is modify the attributes from that class

`car.py`
```Python
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    
    def get_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
```
To see _Getters_ and _Setters_ &rarr; check `practice.py`

- - -

**Setting a Default Value for an attribute**

Attributes can be defined without being passed in as a param
`car.py`
```Python
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
```

- - - 

**Modifying Attribute Values**

1. Direct Modification
The simplest way to modify an attribute is to access it through an instance 

`car.py`
```Python
my_new_car.odometer_reading = 23
```

2. Using a _Setter_ 
It can be helpful to have methods that update certain attributes (Setters)

`practice.py`
```Python
    # setters
    def set_username(self, username):
        self.username = username
    

    def set_id(self, id):
        self.id = id
```

**Incrementing Attribute Values**

1. Through a method
`car.py`
```Python
    def increment_odometer(self, miles):
        self.odometer_reading += miles
```

2. Directly 
```Python
my_new_car.odometer_reading += miles
```

_NOTE_: You can use methods to control modifications to attributes,
but anyone w/ access to your program can modify it directly 

- Effective Security takes time and attention to detail in addition to basic checks

- - -

##### Inheritance

You don't have to start from scratch when writing a class, 
if it's a specialized version of another class

You can use _inheritance_.
* When one class inherits from another
    - It takes on the attributes and methods from the 1st class

* The original class is called the _Parent_ and the new class is the _Child_

- The child inherits methods and attributes from the parent
- The child can define new attributes and methods 

**`__init__()` method for a child class**

When writing a chile class, you'll want to call the `__init__()` method from the parent

`electric_car.py`
```Python
class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    
    def get_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represents aspects of a car, specific to EV's"""

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
```

* When you create a child class, the parent class must be apart of the current file and must appear before the child

- The name of the parent class must be included in the definition of the child class


- `super()` is a function that allows you to call a method from the parent class


**Defining attributes and methods for the child class**

`electric_car.py`
```Python
class ElectricCar(Car):
    """Represents aspects of a car, specific to EV's"""

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery_size = 40

    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
```

**Overriding Methods from the Parent Class**

You can override any method from the parent that doesn't fit what you're trying to model with the child class

To do this: Define a method with the _SAME NAME_ as the parent class
- Python will disregard the parent class method 

`electric_car.py`
```Python
class Car:
        def fill_gas_tank(self):
        print(f"Filling {self.get_name()} w/ GAS!")
...
...
class ElectricCar(Car):
    """Represents aspects of a car, specific to EV's"""

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery_size = 40

    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("EV's don't take GAS!")
```

**Instances as Attributes**

Sometimes, modeling real-world things in code, a growing list of attributes may become lengthy

In this case, one part of a class can be its own separate class. This is called _Composition_ 

`electric_car.py`
```Python
class Car:
    class Battery:
        def __init__(self, battery_size=40):
            self.battery_size = battery_size
        
        def describe_battery(self):
            print(f"This car has a {self.battery_size}-kWh battery")
... 
class ElectricCar(Car):
    """Represents aspects of a car, specific to EV's"""

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = self.Battery()
```

* `Battery` doesn't inherit from any other class

* `ElectricCar` has an attribute called `self.battery` that creates a new instance with a default val from the `Battery` `__init__()`

- - - 

* As you begin to model more complicated things, you'll wrestle w/ complicated questions 
- When you wrestle with implementations as it pertains to real-world objects, focus shifts to logic rather than syntax
- You realze there are no right or wrong approaches to modeling real-world situations
- Some are more efficient than others

- It takes practice to find the most efficient representations

- - - 

###### Importing Classes

To keep your files uncluttered, store your classes in modules and import them into your main program

**Importing a Single Class**

`house.py`
```Python
class House:

    def __init__(self, size, people):
        self.size = size
        self.people = people

    def get_size(self):
        return self.size 
    
    def get_ppl(self):
        return self.people
```

`my_house.py`
```Python
from house import House 

my_house = House('L', 22)
```

**Importing Multiple Classes**

`my_house.py`

```Python
from house import House, Car
```


**Importing All Classes from a Module**

`my_house.py`

```Python

from house import *

```

- This method isn't reccomended
    1. its helpful to read the imports to get a sense of what classes a program uses
        - this approach makes it unclear 
    2. this can also lead to confusion with names in the file
    - naming conflicts w/ classes w/ the same name in your program file
    - can lead to errors 

* IF you need to import many classes from a module
    - Import the entire module 
    - use the `module_name.ClassName` syntax


**Importing a module into a Module**

`modules/electric_car.py`

```Python
from car import Car

class ElectricCar(Car):
    """Represents aspects of a car, specific to EV's"""

    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = super().Battery()

    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        print("EV's don't take GAS!")
```

`my_cars.py`

```Python
from car import Car
from electric_car import ElectricCar
```

- - - 

##### Using Aliases

* You can use aliases when importing classes

_Example_

```Python
from electric_car import ElectricCar as EC

my_leaf = EC('nissan', 'leaf', 2024)
```

**_Giving an entire module an alias_**

```Python
import electric_car as ec
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
```
- - - 

##### Finding your own workflow

Python gives you many options for how to structure code in a large project
It's important to know them so you can use them in your own project 

* When starting out, keep structure simple
    - Do everything in one file 
    - Move classes to separate modules once everything is working

* If you like how modules and files interact, store your classes in modules when starting a project

Find an approach that works, go from there 

- - -

## Python Standard Library

The _Python Standard Library_ is a set of modules included with every Python installation

* You can use an `import` statement at the top of your file

_Example_

* `randint()` takes two ints and returns a random num between the two ints
* `choice()` takes a list/tuple and returns a randomly chosen element

`pstdl.py`
```Python
from random import randint, choice

my_list = [34, 55,6, 466]

print(choice(my_list))
print(randint(1, 3))
```

- - - 

##### Styling Classes

* Classes should be written in _CamelCase_

* Every class should have a docstring immediately following the class definition
    - Brief Description of what the class does
    - Each module should have docstring describing what classes in a module can be used for

* Use blank lines to organize code
    - dont use them excessively 

    - Use one blank line between methods
    - Within module, use 2 blank lines to separate classes

* If you need to import a module from STL, place import for the stl module first
    - then add blank line and import for the import statement for the module you wrote 