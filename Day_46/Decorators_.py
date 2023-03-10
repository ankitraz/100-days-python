



def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        # fx()
        fx(*args,**kwargs)
        print("Thanks for using this function.")
    return mfx



@greet  # decorator function--> it will modify hello function and return that new mfx 
def hello():
    print("hello world")



@greet
def add(a,b):  # we need to provide arguments to greet function as well
    print(a+b)



# hello()
add(3,5)