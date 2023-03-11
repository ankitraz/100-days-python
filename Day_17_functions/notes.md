# Functions
functions in python are defined using the `def` keyword. The syntax is as follows:
```python
def function_name(parameters):
    """docstring"""
    statement(s)
```

## Points to remember
* we can define a function to take any number of arguments, including none at all.
* we can define a function to return any number of values, including none at all.
* we can also specify which arguments are optional and which are required.
* we can also specify which type of arguments are required.
EG. `def function_name(a, b, c=0, d=0):`
```python
def function_name(a:str , b): #a is a string, b is anything
    """docstring"""
    statement(s)
```

## Scope
* The scope of a variable is the region of the program where the variable is recognized.
* The scope of a variable is determined by the block in which it is declared.
* The scope of a variable is local to the block in which it is declared.
* The scope of a variable is global if it is declared outside of all blocks.

Overall, Functions are a great way to reuse code and make your code more readable. They are also a great way to break down large problems into smaller ones.