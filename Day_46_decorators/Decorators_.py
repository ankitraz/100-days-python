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


# creating new decorator 
def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return f"<b>${result}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args,**kwargs)
        return f"<i>${result}</i>"
    return wrapper


@bold
@italic
def welcome(name):
    return f"Hello {name}!"

print(welcome("Ankit"))