from pathlib import Path


# # now we can create path objects 

# Path("C:\\Program Files\\Microsoft") # this is a little bit ugly
# Path(r"C:\Program Files\Microsoft") # using raw string we dont need to use double slashes( for windows)

# # we can also create a path object that represents the current folder
# Path()


# using relative path
path = Path("ecommerce/__init__.py")
# method of path object
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("test.txt")
print(path)
path = path.with_suffix(".txt")
print(path)





# Path() / "ecommerce" / "__init__.py"  # we can also use this

# print(Path.home()) # represents the home directory of user


