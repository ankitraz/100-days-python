# this is intra package reference
print("customer initialized")


#it will print when importing  it
# name of the module can be accessed by 
print("customer initiallized", __name__)  # this will show name as well.


# we can also use if __name__ = "__main__" in modules and not here. and make that module executable 