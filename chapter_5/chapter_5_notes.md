# Chapter 5: `if` Statements 

An expression that can be evaluated as `True` or `False` is called a _conditional test_. 

* If the code in an if statement comes out to `True`, Python executes the code, otherwise, it is ignored

`==` &rarr; equality operator. 
* Returns `True` if vals on the left and right match & `False` if they don't 

Testing for equality is Case Sensitive
_Example_
```Python
car = 'Audi' 
car == 'audi' # Returns false

car.lower() == 'audi' # Returns true 
```

* Websites enforce rules for data that users enter in a similar manner
    - ensure unique usernames 


* `!=` &rarr; inequality operator
    - If two vals do NOT match, Python returns `True`