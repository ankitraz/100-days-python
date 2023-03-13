# Working with Path in Python
* For working with path we need to import `path` module first: 
```python
from pathlib import Path
```

* ### Now we can create a path object
```python
Path("C:\\Program Files\\Microsoft")
# this is not a good way to create a path object as it consist of double backslash after strings
# so we can use raw string to create a path object
Path(r"C:\Program Files\Microsoft")

# now just refer it to a variable and use its method
paths = path(r"C:\Program Files\Microsoft")
```


## Methods of Path object
* ### `Path.cwd()`
```python
Path.cwd()
# this will return the current working directory
```
* ### `Path.exists()`
```python
from pathlib import Path
path = Path("emails")
path.exists()
# this will return True if the path exists
```
* ### `Path.is_file()`
```python
path.is_file() # note that path is a variable which is a path object

# this will return True if the path is a file
```
* ### `Path.is_dir()`
```python
path.is_dir()
# this will return True if the path is a directory
```

* `path.name` will return the name of the file or directory
* `path.stem` will return the name of the file or directory without extension
* `path.suffix` will return the extension of the file or directory
* `path.parent` will return the parent directory of the file or directory

* ### `Path.home()`
```python
Path.home()
# this will return the home directory of the user
```

## Using Relative and Absolute Path
```python
path = Path("ecommerce/__init__.py")
# or we can also use this
path = Path() / "ecommerce" / "__init__.py"
```
```python
path = Path("C:\\Program Files\\Microsoft")
# Absolute path
```