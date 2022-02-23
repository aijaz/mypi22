# Python Notes

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

## Asking for input

- Use `input` to ask the user to input something:

    ```python
    name = input("What is your name?")
    print(name)
