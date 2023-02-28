# def gmean(a,b):
#     return (a*b)/(a-b)

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# print("Geometric Mean: ", gmean(a,b))



# functions in python are defined using the def keyword
# functions can be called using the function name followed by parenthesis
# functions can have parameters
# parameters are variables that are used inside the function
# parameters are passed to the function when it is called
# parameters are separated by commas
# parameters can have default values
# default values are used when the function is called without the parameter


# functions with default values

def add(a=5, b=0):
    return a+b

# print("Addition: ", add())



# using pass keyword in functions

def something():
    pass   # pass keyword is used when we want to define a function but not write any code inside it


# function to print the sum of all numbers in a 
def Sum_all(L):
    _sum = 0;
    for i in L:
        _sum += i
    print(_sum)

v1 = [2,5,6,6]
# Sum_all(v1)




# There are four types of argument in python
# Default Argument, keyword argument, variable length argument, and required argument


# variable length argument

def add(*args):   # *args is used to pass variable length arguments meaning we can pass any number of arguments
    _sum = 0
    for i in args:
        _sum += i
    print(_sum)


add(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)