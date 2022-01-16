# Syllabus & Lesson Plan

We will be using [Python Crash Course, 2nd Edition](https://nostarch.com/pythoncrashcourse2e/) as the course textbook. The syllabus (mostly) follows the order of topics as introduced in the book. I will be using different examples during class so you can use the book to study the topics in greater detail, and get a better understanding of them.

## Setup
- Reboot computer
- Make sure new battery is in camera
- Launch Pycharm
- Close all Pycharm windows
- Quit Pycharm
- Delete wk01
- Launch screenflow start recording
    + Make sure screenflow is recording audio and video
- Launch zoom
    + Make sure zoom is recording
- Do clapper
- Stop Screenflow confirm video is good
- Restart screenflow
- Set focus on Fuji webcam

## Week 1
* Welcome
    - About me
    - About MYPI
        + Two sisters
        + Originally for girls
        + I do outdoor stuff
    - What you'll learn in this class
        + Programming with Python
        + Good enough to interview
* House Rules
    - Feel free to interrupt
        + Just unmute yourself
        + Or raise your hand
    - I'll feel free to tell you to hold on
    - It's ok to say I don't understand 
        + That's on me, not on you
        + Different ways to explain work with different people
    - It's up to you if you want to turn your video on or not
        + It's easier for me to judge if you're confused about something if your video is on. 
        + But at the end it's up to you, and I won't be offended one way or the other
    - Office hours
* Computers are stupid
    * Order
    * Explicit instructions 
    * Only understand very simple languages
* Launching and using the REPL
    * Your first Python Program in the repl
    * Print("hello world")
    * Now you're a programmer
* Pycharm
    * Launch
    * Creating a new project.
    * Type in hello_world.py 
    * How to run the current file
    * Add a second print statement 
* What happens when you run a program
* Syntax highlighting

--- 

* Variables
    * Use a sheet of paper, folded up
    * Two sheets. Give a sheet to each student
    * Ask student to unfold and read the value
    * Use wrong name: Computers are stupid
    * Update variable repeat
    * Message = "hw" print message 
    * Try invalid variable names
        * starting with number
        * With space
        * Typos
    * Assignment 
    * Lookup
    * Give a student a blank sheet. None.
    * Multiple assignment
* Strings
* Operators 
    * print "hello " + "world" string
    * Introduce Integers
    * Int operators
* Functions - title(), upper(), and lower()
* Use pycharm
* "Hello world".title()
* Using variables in strings: f strings
* New lines in strings
* Quotes in strings
* Double and triple quoted strings 
* Comments 
    * why use comments?
* Reading User Input 
* Putting it all together

    ```python
    import pyttsx3
    what = input("What should I say? ")
    engine = pyttsx3.init()
    engine.say(what)
    engine.runAndWait()
    ```

* **Homework**
    * Babyshark.py
    * Write a program that asks you to input a string. Once you input a string it should print out that string, followed by "shark! Do do do, do do do!" 3 times followed by the string, and then "shark"

    ```
        What is your name? 
        Baby
        Baby shark! Do do do do do do!
        Baby shark! Do do do do do do!
        Baby shark! Do do do do do do!
        BABY SHARK!
    ```
    
## Week 2: Introduction to Lists and Tuples

#### Did not finish last week:
* Using variables in strings: f strings
* New lines in strings
* Quotes in strings
* Double and triple quoted strings 
* Putting it all together

    ```python
    import pyttsx3
    what = input("What should I say? ")
    engine = pyttsx3.init()
    engine.say(what)
    engine.runAndWait()
    ```

- Homework review

    ```python
    name = input("What is your name? ")
    print(name + " shark! Do do do do do do!")
    print(name + " shark! Do do do do do do!")
    print(name + " shark! Do do do do do do!")
    print(name.upper() + " SHARK!")    
    ```

- Anything we missed last week

* What is a list
* Accessing elements with indexes
    * index 0 refers to the first item in the list
    * It's this way in most computer languages
    * Think of an index as the _distance from the first item_
    * The index of the last item is the length of the list - 1

        ```python
        my_list = [10, 20, 30]
        l = len(my_list)
        my_list[0]
        my_list[1]
        my_list[2]
        my_list[3] # this should throw an error. Talk about this
        ```

    * You can also use negative indexes. `-1` for the last item, and so on
    * `li = things[-1]`
    * Why `-1`?  Because `-0` doesn't make sense.
* Changing, adding, and removing elements
    * modifying elements 
    * Adding elements `append`
    * `insert(0, "abc")`
    * `l = things.pop()`
    * `a = things.pop(3)`
    * `things.del(3)`
    * `things.remove('a thing')`
    * `l1.extend(l2)` 
* Organizing a list
    * Sort permanently with `sort`
    * Get a sorted copy with `sorted()`
    * Reversing a list with `reverse()`
* `n = len(things)` 
* Tuples
    * Parens 
    * Safety check
    * Usually heterogenous
* Lists containing lists
    * `l1.append(l2)`
    * List data structures
        * [x,y]
        * If you never need to add or delete, use tuples instead 
* List copy references 
    * References
    * Make a "book" of folded sheets of paper
    * Have one student "hold" it with a string
    * Have another student hold onto it as well
    * Update the value in one of the folded sheets 
    * Ask each student to read out their value written on the paper
    * Explain that the strings are references and that the students are variables
    * Making a copy with `l2 = list(l1)`
    * Get a second blank book and copy the values from one book to another
    * Repeat the exercise with lists of lists (books containing books)
* *Homework* 
    1. Make a list of your favorite sports in order of preference (most favorite first)
    2. Print the list
    3. Print the list in reverse order
    4. You learn about a new game called "7 tiles" and suddenly it's your favorite game. Modify the list so that this is new game is now in the first spot, with everything else moving down a spot
    5. After a week, "7 tiles" moves to the second spot but the third most favorite game moves to the top spot. Modify the list accordingly. 
    6. After another week, you get bored of "7 tiles altogether" and remove it from your list altogether. Everything else stays the same. Modify the list accordingly
    7. In a few weeks we'll be making a downhill skiing game. In this game the player will have to ski  between obstacles. Each horizontal row across the slope has 15 spots. Each spot can either have an obstacle or be empty. The goal of the game is to have the player ski through the empty spots without hitting an obstacle. Each obstacle can be a rock or a snowman. You may use strings or integers to represent an obstacle or  an empty space. 
        1. create a data structure for a row. 
        2. Assuming each screen has 20 rows, create a data structure for a screen. 
        3. Assuming each row has 3 obstacles, populate each row with obstacles placed at random locations. 
        4. Print your data structure. 
        5. [image:2C7C6F73-6F2D-4C70-BF73-83D43674D4AB-821-000003A618A42113/IMG_0003.jpeg]


## Week 3. Working with Lists and Tuples

* Homework review
* Looping through an entire list

    ```python
    things = ['Raindrops', 'Whiskers', 'Kettles', 'Mittens', 'Packages']
    for thing in things:
        print(thing)
    ```

* Step through loop
* Multiple statements in a block
    - 2 print statements

* Statements after a for loop

    ```python
    for person in ("Aijaz", "Adel", "Ayesha"):
        print(f"Hello, {person}")
        
    print("It's good to meet all of you.")
        
    the_sum = 0
    for n in (1, 2, 3, 4):
        the_sum = the_sum + n
        
    print(f"The sum of the first 4 integers is {the_sum}")
    ```

* Blank line optional
* Avoiding Indentation Errors
* Making Numerical Lists
    - Many reasons exist: games, measurements, etc.
    - Range
        + Two parameters: start_at and stop_before
        + Never includes the second parameter

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

        + `range` with 1 parameter

            ```python
            for n in range(5):
                print(n)
            ```

        + `range` with 1 parameter - starts at 0, stops at parameter - Works well with list indexes

            ```python
            odds = [1, 3, 5, 7, 9]
            for f in range(len(odds)):
                print(odds[f] + 1)
            ``` 

        + `range` with 3 parameter: increment by parameter 3 instead of 1

            ```python
            for v in range(1, 10, 3):
                print(v)
            ```

        + Using `range` to create lists

            ```python
            l = list(range(1, 10, 3))
            ```

* Functions on lists
    - `min()`
    - `max()`
    - `sum()`
    - `len()`

* List comprehensions
    - Elegant shorthand for the creation of a new list and a `for` loop.

        ```python
        numbers = [1, 2, 3, 4, 5]
        doubles = [x * 2 for x in numbers]
        triples = [item * 3 for item in numbers]
        halves = [item/2 for item in numbers]
        ``` 

    - You can also use ranges with list comprehensions

        ```python
        squares = [x**2 for x in range(1, 10)]
        ```

* List slices
    - A slice is like a range for lists
    - A slice returns a new list

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        first_3 = months[0:3] # ['Jan', 'Feb', 'Mar']
        q2 = months[3:6] # ['Apr', 'May', 'Jun']
        ```

    - Omitting the first parameter implies it's 0

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        first_third = months[:4] # ['Jan', 'Feb', 'Mar', 'Apr']
        ```

    - Omitting the second parameter implies it's the last index + 1

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        last_third = months[8:4] # ['Sep', 'Oct', 'Nov', 'Dec']
        ```

    - Omitting both parameter implies indexes 0 and the last index + 1

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        year = months[:]
        ```

    - An index of -1 is the index of the last item
    - An index of -2 is the second-last item, and so on

        ```python
        months =   ['Jan', 'Feb', 'Mar', 
                    'Apr', 'May', 'Jun', 
                    'Jul', 'Aug', 'Sep', 
                    'Oct', 'Nov', 'Dec']
        p4 = months[-4:-1] # ['Sep', 'Oct', 'Nov']
        ```

* **Homework**

    1. Create a data structure to represent a planet and it's confirmed number of moons. Create a list of these data structures. You can find the data on [Wikipedia](https://en.wikipedia.org/wiki/Planet#Planetary_attributes)
    2. Print the name of each planet along with its number of confirmed moons. 
    3. Print the total number of confirmed moons in the solar system. 
    4. For each of the the first 4 planets in the solar system, print the planet's name, and it's number of moons. Print the total number of moons for those 4 planets.
    5. For each of the the last 3 planets in the solar system, print the planet's name, and it's number of moons. Print the total number of moons for those 3 planets.
    6. Use a single Python statement no more than 80 characters long to generate a list of of the reciprocals of the first 1000 positive integers. (Remember: a positive integer is any whole number greater than 0, and the reciprocal of n is 1/n).


## Week 4. Conditionals

* Programs so far have been boring
* Programs get interesting when they examine conditions and make decisions based on the value of those conditions.
* If statements

    ```python
    team = input("What is your favorite NBA team?")
    if team == "Bulls":
        print("They're my favorite team, too!")
    else:
        print("They're not as good as the Bulls, NGL")
    ```

* Assignment vs Test for equality 

    ```python
    team = 'Bulls'
    team == 'Bulls'
    team == 'Nuggets'
    ```

* Syntactic VS Semantic equality

    ```python
    team = 'Lakers'
    team == 'Lakers'
    team == 'lakers'
    lower(team) 
    lower(team) == 'lakers'
    team = 'LAKERS'
    lower(team) == 'lakers'
    team = 'lAkERs'
    lower(team) == 'lakers'
    team == 'lAkERs'
    ```

* Testing for inequality

    ```python
    team = input("What is your favorite NBA team?")
    if team != "Bulls":
        print("They're not as good as the Bulls, NGL")
    else:
        print("They're my favorite team, too!")
    ```

* Testing numbers

    ```python
    age = input('How old are you?')
    if age > 17:
        print('You are an adult')
    else: 
        print("You're still a child.")
    ```

* Testing multiple conditions

    ```python
    age = input('How old are you?')
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
        print("You can drive!")
    elif age == 18:
        print("You can vote!")
    ```

* Checking multiple conditions
    - Use `or` if you want to check multiple conditions and want to at least one condition to be True

        ```python
        age = input('How old are you?')
        if age < 20 and age > 17: 
            print("You are a teenaged adult.")
        ```

    - Use `and` if you want to check multiple conditions and want to all conditions to be True

        ```python
        age = input('How old are you?')
        if age < 20 and age > 17: 
            print("You are a teenaged adult.")
        ```
* Everything between the `if` and the `:` is called a Boolean expression
* A boolean expression can be composed of other Boolean expressions (like we just saw with `or` and `and`
* Other boolean tests
    - `"Feb" in ["Jan", "Feb", "Mar"]`
    - `"Jun" in ["Jan", "Feb", "Mar"]`
    - `"feb" not in ["Jan", "Feb", "Mar"]`
    - `"ear" in "hearing"`
    - `5 >= 4`
* Describe the modulo operator (`%`)
    - `5 % 3` has the value of the _remainder_ when you divide 5 by 3 (in this case: 2)
    - if `x % y == 0` it means that `x` is a multiple of `y`
    - this is often used to test if a number is odd or even. If that number % 2 is 0, then it is a multiple if 2. Which makes it even. Otherwise that number % 2 is 1, and that makes it odd.
    - The value of `x % y` is always a number >= 0 and less than `y`
* Knowing this, now you can also limit which items make it into a comprehension using a comprehension condition:

    ```python
    squares_of_evens = [x**2 for x in range(1,10) if x%2 == 0]
    ```
    
## While loops

* Backbone of most software
* Example: Loop variable

    ```python
    current_number = 10
    while current_number >= 0:
        print(current_number)
        current_number -= 1
    print("Liftoff!")
    ```

* Example: Break

    ```python
    current_number = 1
    while True:
        print(current_number)
        current_number += 1
        if current_number == 7:
            break
            
    print("Done!")
    ```

    - If you forget the break statement you'll wind up with an infinite loop. You'll have to hit ctrl-C to stop the program
    
    - Looping over a list

        ``` python
        people = ["Alice", "Bob", "Charlie"]
        for person in people:
            print(person)
        ```
        
        + Sometimes we want the index of the item along with the item:

            ``` python
            people = ["Alice", "Bob", "Charlie"]
            i = 0
            for person in people:
                print(f"The person at index {i} is {person}")
                i += 1
            ```
        
        + Since this a common thing to want to do, there's a shortcut to do this in python:

            ``` python
            people = ["Alice", "Bob", "Charlie"]
            for thing in enumerate(people):
                print(thing)
            ```

            ``` python
            people = ["Alice", "Bob", "Charlie"]
            for i, person in enumerate(people):
                print(f"The person at index {i} is {person}")
            ```
            
### Homework

* Let's expand on our game from a couple of weeks ago. 
* Our screen will be 470 pixels wide and 620 pixels high.
* To keep things neat we will have a 10 pixel padding on each end. So our hill will be 450 pixels wide and 600 pixels high.
* In pygame the origin of the coordinate system is at the upper left-hand-side of the screen. This means that the hill is at coordinate (10, 10)
* We will use an image to represent the rider and the flags. The image for the rider will be 30 pixels wide and 30 pixels high. The image for the flag will be 15 pixels wide and 30 pixels high.
* To place any image on the screen we have to specify its bounding rectangle, or rect. There are many ways to specify a rect. The simplest is with a tuple of 4 elements: `(x, y, width, height)` where `x` and `y` represent the location of the upper left hand corner of the image.
* Let's track the x location of the rider with a variable named `rider_x`
* Write code to make sure that the rider stays on the hill and does not go too far off to the right or left. If the rider gets to the left edge of the hill, they can't go any further and stay there. Similarly, the rider cannot go off the right edge of the hill.


## Week 5. Dictionaries
* Creating dictionaries
* Working with dictionaries
* Looping through dictionaries
* Nesting

## Week 6. Loops
* While Loops
* Loops with lists and dictionaries

## Week 7. Making your own Functions
* Defining a function
* Passing arguments
* Return values
* Passing a list
* Passing an arbitrary number of Arguments
* Storing your functions in modules
* Doc strings

## Week 8. Classes
* Creating and using a class
* Working with classes and instances
* Inheritance
* Importing classes
* The Python Standard Library

## Week 9. Files and Exceptions
* Reading from a file
* Writing to a file
* Exceptions
* Storing Data

## Week 10. Introducing PyGame

## Week 11. Project Work

## Week 12. Project Work

## Week 13. Project Work

## Week 14. Project Work

## Week 15. Project Work

## Week 16. Project Work

