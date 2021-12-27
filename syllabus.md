# Syllabus & Lesson Plan

We will be using [Python Crash Course, 2nd Edition](https://nostarch.com/pythoncrashcourse2e/) as the course textbook. The syllabus (mostly) follows the order of topics as introduced in the book. I will be using different examples during class so you can use the book to study the topics in greater detail, and get a better understanding of them.

## Week 1

* Computers are stupid
	* Order
	* Explicit instructions 
* Launching and using the REPL
	* Your first Python Program in the repl
	* Print(“hello world”)
	* Now you’re a programmer
* Pycharm
	* Launch
	* Creating a new project.
	* Type in hello_world.py 
	* How to run the current file
	* Add a second print statement 
* What happens when you run a program
* Operators and objects
	* Objects are things
* Functions
	* Verbs. Actions.
* Saywhat.py

--- 

* Variables
	* Use a sheet of paper, folded up
	* Two sheets. Give a sheet to each student
	* Ask student to unfold and read the value
	* Use wrong name: Computers are stupid
	* Update variable repeat
	* Message = “hw” print message 
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
	* print “hello “ + “world” string
	* Introduce Integers
	* Int operators
* Functions - title(), upper(), and lower()
* Use pycharm
* “Hello world”.title()
* Using variables in strings: f strings
* New lines in strings
* Quotes in strings
* Double and triple quoted strings 
* Comments 
	* why use comments?
* Reading User Input 
* **Homework**
    * Babyshark.py
    * Write a program that asks you to input a string. Once you input a string it should print out that string, followed by “shark! Do do do, do do do!” 3 times followed by the string, and then “shark”
```
	What is your name? 
	Baby
	Baby shark! Do do do do do do!
	Baby shark! Do do do do do do!
	Baby shark! Do do do do do do!
	BABY SHARK!
```
	
## Week 2: Introduction to Lists and Tuples

* What is a list
* Accessing elements
    * index positions
* Changing, adding, and removing elements
    * modifying elements 
    * Adding elements `append`
    * `insert(0, “abc”)`
    * `l = things.pop()`
    * `a = things.pop(3)`
    * `things.del(3)`
    * `things.remove(‘a thing’)`
    * `l1.extend(l2)` 
* Organizing a list
    * Sort permanently with `sort`
    * Get a sorted copy with `sorted()`
    * Reversing a list with `reverse()`
* `n = len(things)` 
* Indexes
    * `li = things[-1]`
* Tuples
    * Parens 
    * Safety check
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
    * Explain that the attings are refernces and that the students are variable
    * Making a copy with `l2 = list(l1)`
    * Get a second blank book and copy the values from one book to another
    * Repeat the exercise with lists of lists (books containing books)
* *Homework* 
    1. Make a list of your favorite sports in order of preference (most favorite first)
    2. Print the list
    3. Print the list in reverse order
    4. You learn about a new game called “7 tiles” and suddenly it’s your favorite game. Modify the list so that this is new game is now in the first spot, with everything else moving down a spot
    5. After a week, “7 tiles” moves to the second spot but the third most favorite game moves to the top spot. Modify the list accordingly. 
    6. After another week, you get bored of “7 tiles altogether” and remove it from your list altogether. Everything else stays the same. Modify the list accordingly
    7. In a few weeks we’ll be making a downhill skiing game. In this game the player will have to ski  between obstacles. Each horizontal row across the slope has 15 spots. Each spot can either have an obstacle or be empty. The goal of the game is to have the player ski through the empty spots without hitting an obstacle. Each obstacle can be a rock or a snowman. You may use strings or integers to represent an obstacle or  an empty space. 
	    1. create a data structure for a row. 
	    2. Assuming each screen has 20 rows, create a data structure for a screen. 
	    3. Assuming each row has 3 obstacles, populate your data structure with the appropriate obstacles
	    4. Print your data structure. 
	    5. [image:2C7C6F73-6F2D-4C70-BF73-83D43674D4AB-821-000003A618A42113/IMG_0003.jpeg]


## Week 3. Working with Lists and Tuples

* Homework review
* Looping through an entire list

```python
for thing in things:
  print(thing)
```

* Step through loop
* Multiple statements in a block
	* 2 print statements
* Statements after a for loop

```python
for person in (“Aijaz”, “Adel”, “Ayesha”):
  print(f”Hello, {person}”)

print(“It’s good to meet all of you.”)

the_sum = 0
for n in (1, 2, 3, 4):
  the_sum = the_sum + n

print(f”The sum of the first 4 integers is {the_sum}”)
```

* 	blank line optional
* Avoiding Indentation Errors
* Making Numerical Lists
	* Many reasons exist: games, measurements, etc.
	* Range
	
```python
s = 0
for v in range(1, 4):
  s = s + v

print(f”the sum of the first 4 integers is {s}”)

#################################################

s = 0
n = 4
for v in range(1, n):
  s = s + v

print(f”the sum of the first n integers is {s}”)

#################################################

s = 0
n = 4
for v in range(1, n):
  s += v

print(f”the sum of the first n integers is {s}”)
```

* Using range to make a list of numbers
* Working with parts of a list

```python
numbers = list(range(1, 5))
```

* **Homework**


## Week 4. Conditionals
* If statements
* Using conditionals with lists

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
