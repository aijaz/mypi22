# Python Notes

# Introduction

## Printing

- Anything in "quotes" is a _string_
- A whole number is an _integer_
- You can print strings or integers this way

    ```python
    # print a string
    print("Hello, world!")

    # print an integer
    print(2)
    ```

- Anything that can be printed is known as an _expression_
- An expression has a value
- The value of a string is the string
- The value of an integer is the integer

## Operations

- An operator is a verb that operates over one or more nouns (operands)
    + `+` is an operator
        * It operates on strings and integers
        * The value of an expression that has an operator is the value of the operation
        
            ```python
            print("Hello, " + "world")  
            # Prints "Hello, world"
            # The value of the expression is the string "Hello, world"
            # That's what's being printed

            print(2 + 3)
            # The value of the expression being printed is 5
            ```

- Operations can use parentheses, like in Math
    
    ```python
    print(2 * (6 - 2))  # prints 8, not 14
    ```

__Remember: If you can print it, it's an expression.__

## Strings

- Strings can be specified with `'single quotes'`, `"double quotes"`, or `"""triple quotes"""`
- Triple-quoted strings can span multiple lines, like this:

    ```python
    poem = """Roses are red,
    I think I am smitten
    Not by Leo
    But this adorable kitten."""
    ```

- If you want to add newlines into a single- or double-quoted string, use the _escape character_ `\n`: 

    ```python
    haiku = "I code in python\nI'm not sure if this will work\nHelp me, Obi-Wan!"
    ```


## Functions

- Functions are commands that do things
- Sometimes functions take _parameters_, like `print(4)` where `4` is the parameter
- Other times functions operate on things like strings. For example:
    + `"hello world".upper()` evaluates to `"HELLO WORLD"`
    + `"hello world".title()` evaluates to `"Hello World"`
    + `"HeLlo wOrlD".lower()` evaluates to `"hello world"`

## Variables

- Variables are things that hold values
- Variables have names so that you can refer to them
- The values that variables hold can be strings, integers, other types, or the special value `None`
- You can assign a value to a variable this way: `my_name = "Aijaz"` or `number_of_surahs = 114`.

## Variables inside strings

- You can insert the values of variables into strings using _f strings_. 
- F strings work with single-, double-, and triple-quoted strings. Use them this way:

    ```python
    my_name = "Aijaz"
    print(f"Hello, {my_name}")
    ```

- Anything inside braces in an f string will be evaluated. 
- Braces can contain any expression.
- Therefore, this is also valid:

    ```python
    my_name = "Aijaz"
    print(f"Hello, {my_name.upper()}!!!")

    # You could also, do this, but it's not as cool:
    print("Hello, " + my_name.upper() + "!!!")
    ```

## Asking for input

- Use `input` to ask the user to input something:

    ```python
    name = input("What is your name?")
    print(name)
    ```

# Lists

- Lists are ordered collections of things.
- Lists can contain all sorts of things, strings, integers, `None`, and other things we haven't seen yet.
- Accessing elements with indexes
    + Lists are _zero-indexed_. This means that the first element in a list is item 0
    + Think of the index of an item as the _distance from the first item_
    + The index of the last item is the length of the list - 1
    + Use `len(l)` to calculate the length of the list named `l`.
    + Create a list with square brackets (see below)
    
        ```python
        my_list = [10, 20, 30]
        l = len(my_list)  # l is equal to 3
        my_list[0]
        my_list[1]
        my_list[2]
        my_list[3]  # this will throw an error. There is no element 3. The last element is element 2.
        ```

    - You can also use negative indexes. `-1` for the last item, and so on
    - `last_item = things[-1]`
    - Why `-1`?  Because `-0` doesn't make sense.
- Changing, adding, and removing elements
    + modifying elements 
    + Adding elements `append`
    + `l.insert(2, "abc")` - insert an element into index 2
    + `item = things.pop()` - return the last item in the list (and remove that item from the list)
    + `a = things.pop(3)` - return the item at index 3 (and remove that item from the  list)
    + `things.del("book")` - remove the item at index 3
    + `things.remove('book')` - remove the first item with a value of `"book"` from the list named `things`
    + `l1.extend(l2)` - add one list to another
- Organizing a list
    + Sort permanently with `cars.sort()`
    + Get a sorted copy with `sorted(cars)`
    + Reverse a list with `cars.reverse()`
- Lists containing lists
