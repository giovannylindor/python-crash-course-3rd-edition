items = ['paris', 'kobe bryant', 'audi']

# sort function 
sort_items = items.sort()
rev_sort = items.sort(reverse=True)

# reverse function
reverse_list = items.reverse()

# append function 
items.append(' jalen brunson ')

# Remove whitespace from last element
player = items[-1].strip().title()


# add element at halfway point
mid_index = int(len(items) / 2)
items.insert(mid_index, 'giovanny lindor')
print(items)

# remove item by val
items.remove('paris')

# pop
last_element = items.pop()

# del
del items[1]

# print final list
print(f"Final List: {sorted(items)}\nTotal Items: {len(items)}")