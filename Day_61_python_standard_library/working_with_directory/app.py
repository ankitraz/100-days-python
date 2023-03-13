from pathlib import Path


path = Path(r"D:\my_workspace\100_days_python\temp")


for p in path.iterdir():  # it gives you all the items in a directory. path.iterdir returns both the file and directory
    # print(p)
    pass


# using list comprehension
paths = [p for p in path.iterdir()]
# print(paths)


# or you can directly use a list
# print(list(path.iterdir()))


# on running above, we will get either windowsPath or posix path.
# windowspath is for windows and posix path is for unix based os


# we can also apply filter to list comprehension to get directories only
paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths)



# for recursive direcetories use this
print(list(path.rglob("*.py")))