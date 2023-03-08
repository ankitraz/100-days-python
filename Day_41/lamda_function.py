# lambda function in python is a small anonyumous function without a name. it is defined using lambda keyword and has the following syntax.

# function to multiply the number by 2
def multiply(num):
    return num*2

# same thing can be done with lambda function in one line
f = lambda num: num*2

print(f(3))


#Lambda functions are commonly used when a small function is needed for a short period of time, such as in a filter, map, or reduce operation. For example, to 
# filter a list of integers to only include even numbers


#In Python, filter() is a built-in function that is used to filter out elements from an iterable (such as a list, tuple, or string) based on a specified condition. It returns a new iterable containing only the elements for which the condition is true.
# filter(function, iterable)  --> syntax for filter function



numbers = [1,2,3,4,5,6,7,8,9,10]
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)