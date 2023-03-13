# Working with directory
* For working with directory we need to import `path` module first: 
```python
from pathlib import Path
```
## To get all the items in a directory
```python 
path = Path("ecommerce")

for p in path.iterdir():
    print(p)
```
* Alternatively, We can also use list comprehension to get all the items in a directory
```python
path = Path("ecommerce")
paths = [p for p in path.iterdir()]
print(paths)
```
* We can use list() to convert the generator from `path.iterdir()` to list
```python
path = Path("ecommerce")
print(list(path.iterdir()))

# output : [PosixPath('ecommerce/__init__.py'), PosixPath('ecommerce/__pycache__'), PosixPath('ecommerce/shipping.py')]
```
*Note:* On running above, we will get either `windowsPath` or `posixpath`.
windowspath is for windows and posix path is for unix based os

## Applying filter on list comprehension to get only files or directories
```python
path = Path("ecommerce")
paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
```

## For listing all the files in a directory or subdirectory
```python
path = Path("ecommerce")
print(list(path.glob("*.*")))

# or you can list a specific type of file
print(list(path.glob("*.py")))
```
*Note:* `glob` is used to list all the files in a directory or subdirectory

*Note:* `*.*` will list all the files in a directory or subdirectory

*Note:* `*.py` will list all the python files in a directory or subdirectory

* We can also use `recursive glob` to list all the files in a directory or subdirectory
```python
path = Path("ecommerce")
print(list(path.rglob("**/*.*")))
```