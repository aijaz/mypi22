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

- Functions on lists
    + `min()`
    + `max()`
    + `sum()`
    + `len()`

- List comprehensions
    + Elegant shorthand for the creation of a new list and a `for` loop.

        ```python
        numbers = [1, 2, 3, 4, 5]
        doubles = [x * 2 for x in numbers]
        triples = [item * 3 for item in numbers]
        halves = [item/2 for item in numbers]
        ``` 

    + You can also use ranges with list comprehensions

        ```python
        squares = [x**2 for x in range(1, 10)]
        ```

- List slices
    + A slice is like a range for lists
    + A slice returns a new list
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        first_3 = months[0:3] # ['Jan', 'Feb', 'Mar']
        q2 = months[3:6] # ['Apr', 'May', 'Jun']
        ```
    
    + Omitting the first parameter implies it's 0
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        first_third = months[:4] # ['Jan', 'Feb', 'Mar', 'Apr']
        ```
    
    + Omitting the second parameter implies it's the last index + 1
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        last_third = months[8:4] # ['Sep', 'Oct', 'Nov', 'Dec']
        ```
    
    + Omitting both parameter implies indexes 0 and the last index + 1
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        year = months[:]
        ```
    
    + An index of -1 is the index of the last item
    + An index of -2 is the second-last item, and so on
    
        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        p4 = months[-4:-1] # ['Sep', 'Oct', 'Nov']
        ```

# Homework:

1. Create a data structure to represent a planet and it's confirmed number of moons. Create a list of these data structures. You can find the data on [Wikipedia](https://en.wikipedia.org/wiki/Planet#Planetary_attributes)
2. Print the name of each planet along with its number of confirmed moons. 
3. Print the total number of confirmed moons in the solar system. 
4. For each of the the first 4 planets in the solar system, print the planet's name, and it's number of moons. Print the total number of moons for those 4 planets.
5. For each of the the last 3 planets in the solar system, print the planet's name, and it's number of moons. Print the total number of moons for those 3 planets.
6. Use a single Python statement no more than 80 characters long to generate a list of of the reciprocals of the first 1000 positive integers. (Remember: a positive integer is any whole number greater than 0, and the reciprocal of n is 1/n).

```python
# 1
planets_and_moons = [
    ('Mercury', 0),
    ('Venus', 0),
    ('Earth', 1),
    ('Mars', 2),
    ('Jupiter', 80),
    ('Saturn', 83),
    ('Uranus', 27),
    ('Neptune', 14),
]

# 2
total = 0
for planet_name, number_of_moons in planets_and_moons:
    print(f"{planet_name} has {number_of_moons} moons")
    total += number_of_moons

# 3
print(f"The total number of confirmed moons in the solar system is {total}")

# 4
total = 0
for planet_name, number_of_moons in planets_and_moons[:4]:
    print(f"{planet_name} has {number_of_moons} moons")
    total += number_of_moons

print(f"The total number of confirmed moons for these planets is {total}")

# 5
total = 0
for planet_name, number_of_moons in planets_and_moons[-3:]:
    print(f"{planet_name} has {number_of_moons} moons")
    total += number_of_moons

print(f"The total number of confirmed moons for these planets is {total}")

# 6
print([1/x for x in range(1, 1001)])

```

## Alternate method (Aqsa's method)

```python
# 1
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
num_moons = [0, 0, 1, 2, 80, 83, 27, 14]

# 2
for index in range(len(planets)):
    print(f'Planet {planets[index]} has {num_moons[index]} moons')

# 3
print(f'The total number of confirmed moons in the solar system is {sum(num_moons)}')

# 4
print(f'The total number of confirmed moons in the solar system is {sum(num_moons[:4])}')

# 5
num_planets = len(planets)
for index in range(num_planets - 3, num_planets):
    print(f'Planet {planets[index]} has {num_moons[index]} moons')
```

# Conditionals

- `if` statements

    ```python
    team = input("What is your favorite NBA team?")
    if team == "Bulls":
        print("They're my favorite team, too!")
    else:
        print("They're not as good as the Bulls, NGL")
    ```

- Assignment vs Test for equality 

    ```python
    team = 'Bulls'     # this is used to set the value of team to 'Bulls'
    team == 'Bulls'    # two equal signs are used to compare values. This is a Boolean expression
    team == 'Nuggets'  # two equal signs are used to compare values. This is a Boolean expression
    ```

- Syntactic VS Semantic equality

    ```python
    team = 'Lakers'
    team == 'Lakers'
    team == 'lakers'
    team.lower() 
    team.lower() == 'lakers'
    team = 'LAKERS'
    team.lower() == 'lakers'
    team = 'lAkERs'
    team.lower() == 'lakers'
    # use .lower() or .upper() or even .title() to compare strings case insensitively
    ```

- Testing for inequality

    ```python
    team = input("What is your favorite NBA team?")
    if team != "Bulls":
        print("They're not as good as the Bulls, NGL")
    else:
        print("They're my favorite team, too!")
    ```

- Testing numbers

    ```python
    age = input('How old are you?')
    age = int(age) # convert the string to an integer
    if age > 17:
        print('You are an adult')
    else: 
        print("You're still a child.")
    ```

- Testing multiple conditions

    ```python
    age = int(input('How old are you?'))  # You can do this all in one statement
    if age < 4: 
        print("You're a baby")
    elif age < 11:
        print("You're a little kid")
    elif age < 13:
        print("You're a tween")
    elif age < 18:
        print("You're a teenager")
    elif age < 20:
        print("You're a teenaged adult")
    else:
        print("You're an adult")
        
    # no else block
    
    if age == 16:
        print("You can drive now!")
    elif age == 18:
        print("You can vote now!")
    ```

- Checking multiple conditions
    - Use `or` if you want to check multiple conditions and want to at least one condition to be True

        ```python
        age = input('How old are you?')
        if age < 13 or age > 19: 
            print("You're not a teenager.")
        ```

    - Use `and` if you want to check multiple conditions and want to all conditions to be True

        ```python
        age = input('How old are you?')
        if age < 20 and age > 17: 
            print("You are a teenaged adult.")
        ```
- Everything between the `if` and the `:` is called a Boolean expression
- A boolean expression can be composed of other Boolean expressions (like we just saw with `or` and `and`)
- Other boolean tests
    + `"Feb" in ["Jan", "Feb", "Mar"]`
    + `"Jun" in ["Jan", "Feb", "Mar"]`
    + `"feb" not in ["Jan", "Feb", "Mar"]`
    + `"ear" in "hearing"`
    + `5 >= 4`
- Describe the modulo operator (`%`)
    + `5 % 3` has the value of the _remainder_ when you divide 5 by 3 (in this case: 2)
    + if `x % y == 0` it means that `x` is a multiple of `y`
    + this is often used to test if a number is odd or even. If that number % 2 is 0, then it is a multiple if 2. Which makes it even. Otherwise that number % 2 is 1, and that makes it odd.
    + The value of `x % y` is always a number >= 0 and less than `y`
- Knowing this, now you can also limit which items make it into a comprehension using a comprehension condition:

    ```python
    squares_of_evens = [x**2 for x in range(1,10) if x%2 == 0]
    ```

# Homework
