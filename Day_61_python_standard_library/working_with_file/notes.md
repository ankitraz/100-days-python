# Working with file

First we need to create a path object which represents a file.

```python
from pathlib import Path

path = Path("ecommerce/__init__.py")

print(path.exists()) # this will check if the file exists or not

path.rename("init.txt")

path.unlink() # this will delete the file

```

## Getting Status of a file
```python
from pathlib import Path
from time import ctime

path = Path("ecommerce/__init__.py")
path.stat() # this will return the status of the file
# it will return in timeofcreation and time of modification

# we need to change the time of creation and modification 
# to human readable format

print(ctime(path.stat().st_ctime)) # this will return the time of creation

```

## Reading and Writing to a file
```python
from pathlib import Path
path = Path("ecommerce/__init__.py")
print(path.read_text()) # this will read the file and return the content of the file

path.write_text("print('hello world')") # this will write the content to the file


# initially we were doing 
# with open("ecommerce/__init__.py") as file:
#    ...

# but path.write_text() will do the same thing as above and it is more readable

```

## Copy a file
```python
from pathlib import Path
path = Path("ecommerce/__init__.py")
path2 = Path() / "ecommerce" / "__init__.py"

path2.write_text(path.read_text()) # this will copy the content of the file

```

### There is an alternative way to copy a file easily
```python
from pathlib import Path
import shutil

path = Path("ecommerce/__init__.py")
path2 = Path() / "ecommerce" / "__init__.py"

shutil.copy(path,path2) # this will copy the file

```