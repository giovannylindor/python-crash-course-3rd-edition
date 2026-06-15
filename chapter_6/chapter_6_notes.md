# Chapter 6: Dictionaries
- - - 

A dictionary is a collection of _key-value_ pairs.
Each key is connected to a value, and you can use a key to access the value associated w that key

Key-Value Pair: Set of values associated with each other
Provide Key &rarr; Python Returns Value 
Keys are connected by a colon 
Individual Key-Value Pairs are separated by commas 

Key can be:
* Number
* String
* List
* Another Dictionary

Syntax: 
_var_ = { _key_ : _value_ , ... ..}

- See `alien.py` for code snippets

##### Accessing Values

To get the value, give the name of the dictionary & place the key inside brackets

_Example_

```Python
alien_0 = {'color': 'green'}
print(alien_0['color']) # Returns "green"
```

* You can have unlimited key-val pairs in a dictionary

##### Adding New Key-Value Pairs

* Dictionaries are dynamic & you can add new k-v pairs at any time
- See `alien.py`

```Python

alien_0['x-pos'] = 35.2
alien_0['y-pos'] = 99.42

print(alien_0)
```

* Dictionaries retain the order in which they are defined. 
    - You see the elements in the same order they were added

##### Empty Dictionary

Sometimes it's convient/necessary to start w/ an empty dict and then adding a new item to it

```Python 
alien_1 = {}
```
* You'll use empty dict when storing user-supplied data or writing code that auto generates large k-v pairs 

##### Modifying Vals

```Python
alien_2 = {'x-positon': 0, 'y-position': 25,
            'speed': 'medium'}

print(f"OG Position: {alien_2['x-positon']}")

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else: 
    x_increment = 3

alien_2['x-positon'] += x_increment
print(f"New Position: {alien_2['x-positon']}")
```

##### Removing Key-Value Pairs

When you no longer need a key-val pair, you can use the `del` keyword
- All `del` needs is the dict name and the key to be removed

```Python
alien_3 = {'color': 'indigo', 'points': 2_354_423}
print(f"\nAlien_3: {alien_3}")

del alien_3['points']
print(f"New Alien_3: {alien_3}")
```

* Deleted K-V pairs are removed _Permanently_ 

##### Dictionary of Smaller Objects
See `favorite_languages.py`

```Python
favorite_languages = {
    'jen': 'python', 
    'sarah': 'c',
    'eddie':'rust',
    'phil': 'python'
}
```

* When you know you'll need more than one line to define a dic, hit ENTER & Indent

##### Using `get()` to Access Values

See `alien_no_points.py`

* Using keys in square brackets may cause an error if you ask for a key that doesn't exist

* `get()` &rarr; sets a default value that'll be returned if a key doesn't exist
    - `arg1`: key youre looking for 
    - `arg2`: value you want if the key doesn't exist 
    - if you omit `arg2`, python will return `None` ("No Value Exists") &rarr; `None` isn't an error, but a special value 

```Python
speed = alien.get('speed', 'FAST')
print(speed)
```

* Consider using the `get()` method when you're looking for keys that may not exist instead of bracket notation

##### Looping through a Dictionary
See `user.py`

**Looping through all Key-Value Pairs**
```Python
for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Val: {value}")
```

* to write a `for` loop in a dictionary
    1. write 2 var names to hold the key and val 
    2. specify the name of the dict followed by `.items()` which returns the key,value pairs
        - the for loop assigns each of the pairs to key and val vars
    ```Python
    for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
    ```

**Looping through ALL KEYS**
- `.keys()` method is used when looping only the keys of a dict
    - it returns all keys from a dictionary

```Python
# Looping through dict (KEYS ONLY)
print("People: ")
for name in favorite_languages:
    print(f"{name}")
# for name in favorite_languages.keys() is the same syntax as the code above ^
```

- Looping through keys is default behavior 
    - You can use `keys()` explicitly to make your code easier to read or you can omit it

```Python
shoes = {
    'nike': 'kobe',
    'jordan': 'zion',
    'converse': 'shai'
}

brands = ['nike', 'converse']

for brand in shoes.keys():
    if brand in brands:
        print(f"{brand.title()}'s Signature Athlete is {shoes[brand].title()}")
    else:
        print(f"{brand}")
```

**Looping through keys in a particular order**
See `sorted_dict.py`

- `sorted()` sorts all the keys in a dictionary 

```Python
shoes = {
    'sga': 'converse', 
    'lebron': 'nike',
    'luka': 'jordan',
    'jokic': '361'
}

for player in sorted(shoes.keys()):
    if player == 'sga':
        print(f"\n{player.upper()} is a {shoes[player]} signature athlete")
    else:
        print(f"\n{player.title()} is a {shoes[player]} signature athlete")
```


**Looping through all vals in a dictionary**
- similar to using the `keys()` method, use the `values()` method to extract all values from a dictionary

See `loop_dict.py`
```Python
d = {
    'SGA': 'converse',
    'LeBron': 'nike',
    'Luka': 'jordan'
}

print(f"The following brands have been mentioned: ")
for brand in d.values():
    print(f"{brand.title()}")
```

- The code above works, but doesn't account for repeat values
    - _set_ &rarr; collection in which EACH item **_MUST_** be unique

```Python
print(f"The following brands have been mentioned: ")
for brand in set(d.values()):
    print(f"{brand.title()}")
```

- `set()` method allows python to identify unqiue items and builds a non-repetative set from those items

* You can build a set using braces, and separating them w/ commas

**NOTE**

* _When working w/ lists, tuples, and dictionaries, if you define a 2 values w/o separating them with a comma, Python concentates them together!!_

##### Nesting

Nesting is when you want to store multiple dicts in a list, and a list inside a dict

**A List of Dictionaries**
- see `aliens.py`
- its common to store a num of dicts in a list where each dict contains info about one object

**A List inside a Dictionary**
- see `pizzas.py`
- its sometimes useful to put a list inside a dictionary
    - see `nba.py` for a personal practice instance
    
**_NOTE_** when you need to break up a long line in a print statement, choose the appropriate 
point, end w/ a quotation mark, break to a new line, add an opening quote, then finish your string 

_Example_

```Python
print(f"You ordered a {pizza['crust']}-crust pizza "
      "w/ the following: ")
```

* You can nest a list inside a dict anytime you want more than one val associated w/ a key in a dictionary
- see `new_lang.py`

**_NOTE_**: Whenever you reference a method without (), Python just shows you what the method is rather than running it. The () is what actually executes the call.

* You shouldn't nest lists and dictionaries too deeply. If youre nesting items too deeply, theres most likely a more _simpler way_ to solve the problem. 


**Dictionary Inside Dictionary** 
* You can nest a dict inside another dict
    - But your code can get complicated

* If you have several users for a website, each w/ a unique username, you can store the usernames as keys in a dictionary
    - then u can store info about each user by using a dictionary as the value

- See `many_users.py`