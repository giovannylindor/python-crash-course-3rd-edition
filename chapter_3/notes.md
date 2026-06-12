# Chapter 3: Lists
- - -

**List**: A collection of items in a particular order
- Allows the storage of sets of information in one place 

_Syntax_
`var_name = ['element', ... ]`

* Lists are 0-indexed, similar to arrays 

* Accessing a list at the index `-1` returns the last element
    - Accesssing a list with `-n` returns the `nth` item from the end  
_Example_
`var_name[n]`

Modifying Elements 
_Syntax_
`var_name[n] = val` 

Adding Elements to a List
`var.append(val)` &rarr; adds element to the end of the list

Inserting Elements at a Position
`var.insert(index, val)` &rarr; adds element at a given index
- This shifts every other value in the list one position to the right 

Removing Elements from a List 
You can use the `del` statement if you know the index 
`pop()` &rarr; removes last item in a list, and returns that val 
- You can pop an item from any position as an arg

**Difference Between `pop()` and `del`**
1. when you want to remove an element and NOT use its val &rarr; `del`
2. if you want use its val &rarr; `pop()`

Removing by Value
Using the `remove(val)` allows you to remove the value from the list
- It's good for when you don't know the index
- It only removes the _FIRST_ occurence of the value