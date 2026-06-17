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

**Using `break`**
- To exit a `while` loop, w/o running any code in the loop, use the `break` statement
    - `break` directs flow of your program
    - can control what lines are executed and what lines aren't
- see `cities.py` 

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