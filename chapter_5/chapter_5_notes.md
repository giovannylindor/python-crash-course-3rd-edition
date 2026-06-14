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


* `and` &rarr; checks if both conditions are both `True`
* `or` &rarr; checks if 1/2 conditions are `True`

- - - 

### Checking if a Value is in a list

* Sometimes it may be important to check whether a value is in a list before doing any major operations
    - I.E: checking if a username already exists

* `in` &rarr; tells Python to check for the existence of a value in a list
```Python
if 1 in vals:
    print(True)
``` 

_Syntax_ 
if _val_ in _list:
...


* `not` &rarr; tells Python to check if a value does NOT appear in a list
```Python
if 1 not in vals:
    print(True)
```

- - - 

### Boolean Expressions

Boolean expression is just another name for a conditional test 
- Either `True` or `False`
- Boolean Vals provide an efficient way to track the state of a program or condition

- - - 

### `if` Statements

Several `if` statements exist and your choice depends on the number of conditions

**Simple `if` Statements**

_Example_ 

if _conditional_test:
    do something

**`if-else` Statements**

Often, you'll want to take one action when a conditional test passes and a different action in all other cases

* `if-else` is similar to `if`, but the else allows you to define an action(s) that execute when the `if` conditional test fails

**`if-elif-else` Chain**

