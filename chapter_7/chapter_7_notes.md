# Chapter 7: User Input and While Loops 
- - - 

* the `input()` function pauses program execution and waits for user input 
    - it takes one arg &rarr; user input

* your `input()` function should include an easy to follow prompt to tell the user what info youre looking for
See `greeter.py`

* `input()` interprets user inputs as strings
    - `int()` converts input string to numerical value
    - see `numerical.py`
    - see `rollercoaster.py`

##### Modulo Operator `%` 
* Returns the remainder of 2 operands 
see `even_or_odd.py`'

##### `while` Loops
- A `while` loop runs until a certain condition is met
see `counting.py` (basic implementation)
see `parrot_2.py`

**Using Flags**
Flag: A variable that determines whether or not the entire program is `True`
* Flag == Signal to a program
    - If any event needs to end the program, the flag can be set to False
    - see `parrot3.py`
```Python
while active: 
    message = input(prompt)
    if message.lower() == 'quit':
        active = False
    else: 
        print(f"Text: {message}")
```

* Flags will finsh the rest of the loop body, but will be checked again after the next iteration 

**Using `break`**
- To exit a `while` loop, w/o running any code in the loop, use the `break` statement
    - `break` directs flow of your program
    - can control what lines are executed and what lines aren't
- see `cities.py` 

* `break` immediately stops loop execution 


**Using `continue` in a Loop**
Rather than breaking out of a loop w/o executing the rest of its code, 
using `continue` can return you to the beginning of the loop

See `counting2.py`
```Python
curr = 0
while curr < 10:
    curr += 1
    if curr % 2 == 0:
        continue
    print(curr)
```

**Avoiding Infinite Loops**
Every loop needs a way to break otherwise, it'll loop forever.
If your program gets stuck in an infinite loop, pressing `CTRL-C` stop the program from running

* To avoid writing infinite loops, test every loop and make sure it stops when you want it to

- - - 
##### Using a `while` loop w/ lists & dictionaries

* `for` loops are effective for looping through a list, but you shouldn't modify a list inside a `for` loop because Python will have trouble keeping track of the items in the list 

To modify a list as you work through it, use a while loop
- They allow you to collect, store, and organize inputs to examine and report on

**Moving items from one list to another**
See `confirmed_users.py`
```Python
while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()
    print(f"Verifying: {current_user.title()}...")
    confirmed_users.append(current_user)

print("\nConfirmed Users:")
for user in confirmed_users:
    print(f"{user.title()}")
```

**Removing all instances of specific vals from a list**
-`remove()` works when you want to remove a singular val from a list 

to remove ALL instances, see `pets.py`
```Python
while 'cat' in pets:
    pets.remove('cat')

print(f"\nNew List: {pets}")
```

**Filling a Dictionary w/ User Input**
See `mountain_poll.py`