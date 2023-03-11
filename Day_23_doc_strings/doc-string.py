# doc-string are the stirng literals that appear right after the definition, mehtod, class or module
# they are used to document our code

def square(n):
    '''it takes a number and returns the square of it'''
    return n**2 # or return n*n


print(square(5))
print(square.__doc__) # this is not a comment. this __docstirng__ is used to fetch the value of docstring.



# docsttring is written just after def fun_name() line, any line between them would lead to none docstring.
