glossary = {
    "None": "Special value indicating the absence of a value",
    "List": "A Heterogenous dynamic array of values",
    "Tuple": "A Heterogenous Array of constant, unchangeable values",
    "Dictionary": "A list of related key-value pairs",
    "Boolean": "A True/False output/expression",
    "Set": "A collection of unique items. Similar to a Dictionary",
    "Conditional": "A statement that executes based on a statement thats deemed true or false",
    "Relational": "An operation that check how one value relates to another", 
    "Primative": "A data type that fundamental and embedded in a programming language",
    "Non-Primative": "A data type built on by the user and is made using a combination of other primative types"
}

for name, definition in glossary.items():
    print(f"\n{name.title()}: {definition}")

