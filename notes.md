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

# Week 1 Homework:

This is week 1's homework:

```python
name = input("What is your name? ")
print(name + " shark! Do do do do do do!")
print(name + " shark! Do do do do do do!")
print(name + " shark! Do do do do do do!")
print(name.upper() + " SHARK!")    
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
- Tuples
    + Tuples are comma-separated values
    + They can optionally have parentheses around them. 
    + This makes them look like lists
    + Unlike lists, however, you cannot add or remove an item from a tuple. Nor can you change an item in a tuple.
    + Tuples are useful for creating data structures (groups of things) that will never change.
- Lists containing lists 
    + Lists can contain lists e.g.: `l = [1, 3, 5, ["Book", "Pen", "Pencil"]]`

# Week 2 Homework

1. Make a list of your favorite sports in order of preference (most favorite first)
2. Print the list
3. You learn about a new game called "7 tiles" and suddenly it's your favorite game. Modify the list so that this is new game is now in the first spot, with everything else moving down a spot. Print the list.
4. After a week, "7 tiles" moves to the second spot but the third most favorite game moves to the top spot. Modify the list accordingly, and print the list.
5. After another week, you get bored of "7 tiles" and remove it from your list altogether. Everything else stays the same. Modify the list accordingly, and print the list.
6. Print the list in reverse order

```python
sports = ['Soccer', 'Cricket', 'Tennis']
print(sports)
sports.insert(0, "7 tiles")
print(sports)
sports.insert(0, sports.pop(2))
print(sports)
sports.remove("7 tiles")
print(sports)
sports.reverse()
print(sports)
```

7. I'm creating an Avatar Fandom page. I want to keep track of the following information for each character: Name, Nationality, Children, Bending. 
    - Every character will have a name and nationality
    - We will keep track of the names of the character's children (if any)
    - Some characters may not have children
    - Some characters will have a single bending power
    - Some characters will have more than one bending power
    - Some characters may not have any bending powers
    - Design a data structure for this fandom page
    - Populate your data structure using the data below
    - Print the value of your data structure
    - This is gonna take some thought, so spend some time on this assignment.
    - Data:
        + Name: Aang
            + Nationality: Southern Air Temple
            + Children: 
                * Bumi
                * Kya
                * Tenzin
            + Bending: 
                * Air
                * Water
                * Earth
                * Fire
                * Energy
        - Name: Katara
            + Nationality: Southern Water Tribe
            + Children:
                * Bumi
                * Kya
                * Tenzin
            + Bending: 
                * Water
                * Blood
        - Name: Sokka
            + Nationality: Southern Water Tribe
            + Children: None
            + Bending: None
        - Name: Toph Beifong
            + Nationality: Gaoling, Earth Kingdom
            + Children: 
                * Lin Beifong
                * Suyin Beifong
            + Bending:
                * Earth
                * Metal
        - Name: Zuko
            + Nationality: Fire Nation Capital, Fire Nation
            + Children: 
                * Izumi
                * Kya
            + Bending:
                * Fire
                * Energy
        - Name: Iroh
            + Nationality: Fire Nation Capital, Fire Nation
            + Children: 
                * Lu Ten
            + Bending:
                * Fire
                * Energy
        - Name: Zhao
            + Nationality: Fire Nation Capital, Fire Nation
            + Children: 
                * None
            + Bending:
                * Fire

```python
data = [
    ['Aang', 'Southern Air Temple', ['Bumi', 'Kya', 'Tenzin'], ['Air', 'Water', 'Earth', 'Fire', 'Energy']],
    ['Katara', 'Southern Water Tribe', ['Bumi', 'Kya', 'Tenzin'], ['Water', 'Blood']],
    ['Sokka', 'Southern Water Tribe', [], []], 
    ['Toph Beifong', 'Gaoling, Earth Kingdom', ['Lin Beifong', 'Suyin Beifong'], ['Earth', 'Metal']],
    ['Zuko', 'Fire Nation Capital, Fire Nation', ['Izumi', 'Kya'], ['Fire', 'Energy']],
    ['Iroh', 'Fire Nation Capital, Fire Nation', ['Lu Ten'], ['Fire', 'Energy']],
    ['Zhao', 'Fire Nation Capital, Fire Nation', [], ['Fire']]
]
print(data)
# Note: I'm using empty lists for children and bending
# for Sokka, instead of None. If I used None, I would 
# interpret that as "I don't know if Sokka has children
# or bending skills". Using the empty lists implies: 
# "I know he has 0 children and 0 bending skills"
```

# Working with Lists and Tuples

- Looping through an entire list:

    ```python
    things = ['Raindrops', 'Whiskers', 'Kettles', 'Mittens', 'Packages']
    for thing in things:
        print(thing)
        print(f"{thing} is one of my favorite things")
    ```

- Statements after a for loop

    ```python
    for person in ("Aijaz", "Adel", "Ayesha"):
        print(f"Hello, {person}")
        
    print("It's good to meet all of you.")
        
    the_sum = 0
    for n in (1, 2, 3, 4):
        the_sum = the_sum + n
        
    print(f"The sum of the first 4 integers is {the_sum}")
    ```

- Making Numerical Lists
    + Many reasons exist: games, measurements, etc.
    + Range
        * Two parameters: _start_at_ and _stop_before_
        * Never includes the second parameter

            ```python
            s = 0
            for v in range(1, 4):
                s = s + v
            
            print(f"the sum of the first 3 integers is {s}")
            
            #################################################
            
            s = 0
            n = 4
            for v in range(1, n):
                s = s + v
            
            print(f"the sum of the first {n - 1} integers is {s}")
            
            #################################################
            
            s = 0
            n = 4
            for v in range(1, n):
                s += v
            
            print(f"the sum of the first {n - 1} integers is {s}")
            ```

        * `range` with 1 parameter

            ```python
            for n in range(5):
                print(n)
            ```

        * `range` with 1 parameter - starts at 0, stops at parameter - Works well with list indexes

            ```python
            odds = [1, 3, 5, 7, 9]
            for f in range(len(odds)):
                print(odds[f] + 1)
            ``` 

        * `range` with 3 parameter: increment by parameter 3 instead of 1

            ```python
            for v in range(1, 10, 3):
                print(v)
            ```

        * Using `range` to create lists

            ```python
            l = list(range(1, 10, 3))
            ```
