# Syllabus & Lesson plan

* Computers are stupid
	* order
	* Explicit instructions 
* Using the REPL
	* Your first Python Program in the repl
	* Print(“hello world”)
	* Now you’re a programmer
* Pycharm
	* launch
	* New project without venv.   
	* Type in hello_world.py 
	* Add a second print statement 
* What happens when u run a program
* Operators and objects
	* objects are things
* Functions
	* verbs.  Actions
* Saywhat.py
* *Break*
* Variables
	* Use a sheet of paper, folded up
	* two sheets give a sheet to each student
	* Ask student value
	* Use wrong name: cas 
	* Update variable repeat
	* Message = “hw” print message 
	* Try invalid variable names
	    * starting with number
	    * With space
	    * Typos
	* Assignment 
	* Lookup
	* Multiple assignment
* Strings
* Operators 
	* + print “h “ + “w” string
	* Int operators
* Functions title, upper lower
* use pycharm
* “H w”.title()
* Using variables in strings: f strings
* New lines in strings
* Quotes in strings
* Double and triple quoted strings 
* Comments 
	* why?
* User Input 
* *Break*
* GitHub 
	* Repositories
	* How to fork & clone
	* Clone pygame repo
	* How to push a pr
* *Homework*
	* read
	    * variable names
	    * String functions
	    * F strings
	* Write
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
	
---
2. Introduction to Lists and Tuples
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
		    * Would never add or delete, so use tuple instead 
    * List copy references 
	    * references
	    * Making a copy with `l2 = list(l1)`
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

	    8. 
---
3. Working with Lists and Tuples
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

#####
s = 0
n = 4
for v in range(1, n):
  s = s + v

print(f”the sum of the first n integers is {s}”)

#####
s = 0
n = 4
for v in range(1, n):
  s += v

print(f”the sum of the first n integers is {s}”)

	# Using range to make a list of numbers
	# Working with parts of a list

numbers = list(range(1, 5))
```
4. Conditionals
    * If statements
    * Using conditionals with lists
5. Dictionaries
    * Creating dictionaries
    * Working with dictionaries
    * Looping through dictionaries
    * Nesting
6. Loops
    * While Loops
    * Loops with lists and dictionaries
7. Making your own Functions
    * Defining a function
    * Passing arguments
    * Return values
    * Passing a list
    * Passing an arbitrary number of Arguments
    * Storing your functions in modules
    * Doc strings
8. Classes
    * Creating and using a class
    * Working with classes and instances
    * Inheritance
    * Importing classes
    * The Python Standard Library
9. Files and Exceptions
    * Reading from a file
    * Writing to a file
    * Exceptions
    * Storing Data
10. Introducing PyGame
11. Project Work
12. Project Work
13. Project Work
14. Project Work
15. Project Work
16. Project Work