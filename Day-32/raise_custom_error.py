usr_input = input("Write 'quit' to quit: ")

if usr_input != "quit":
    raise ValueError("you did't specified whether to quit or not.")
else:
    print("Program sucessfully quit.")



# in above we raised our own error from built in python error.
# however we can also create our own error.


class CustomError(Exception):
    #code...
    pass


try:
    #code
    pass
except CustomError: # using that custom created error
    #code
    pass