# Chapter 4: Working with Lists
- - -

* `list()` &rarr; creates a list

#### `for` Loops

`for` loop syntax
`for` [_value_] `in` _list_:
    (_Operations_)

* This loop goes from the beginning of the list to the end
similiar to `for(int i = 0; i < n; i++)`

- Indentation after colon &rarr; method/loop body

* `range(start, end)` &rarr; generages a series of vals from the starting val to the end - 1
    - `start` and `step` args are optional 
    - adding a 3rd arg (`range(start, end, step))`) is an increment arg. increments the range by _step_ numbers.


* `min(list)` &rarr; returns the lowest val in a list (`string` & `int`)
* `max(list)` &rarr; returns the largest val in a list (`string` & `int`)
* `sum(list)` &rarr; returns the sum of all elements in a list (works w/ number-based lists)


**List Comprehension:** Generating a list in one line of code
- Combines `for` loop and creating of new elements in one line
- Seen in other peoples code
_Syntax_
```Python

squares = [value ** 2 for value in range(1, 11)]
# for numbers 1-10, raise each value to the power of 2 
```
- - -

### Slicing

- To slice, specify the index of the 1st and last elements
- Similar to range, python stops before the second specified index

_Syntax_
_list_[_val1_:_val2_] &rarr; extracts elements from val1 to [val2 - 1]

- If you omit val1, python starts from the beginning of the list to [val2 - 1]
- If you omit val2, pyhton goes from val1 to the end of the list

- You can add a 3rd arg (_step_), which tells python how many items to skips in the range



* In web dev &rarr; you can use slices to display info in a series of pages w/ appropriate info in each page

- - -

### Copying Lists

* To copy a list, make a slcie that includes the entire list by omitting `val1` and `val2`
_list_ = _list2_[:]

* `list1 = list2` is NOT a copy &rarr; you're having `list1` point to `list2`
    - Any modifications go directly to both lists