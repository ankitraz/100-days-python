# Working with zip files

There is a module in python to work with zip files. We can use this module to `create`, `extract`, `add`, `remove` files from zip files.


## Creating a zip file

```python
from zipfile import ZipFile

zip = ZipFile('files.zip', 'w') # w is for write mode

# add files to the zip file

iterator = Path("ecommerce").rglob("*.*") # this will return a generator object which will iterate over all the files in the directory

for file in iterator:
    zip.write(file) # this will add the file to the zip file
zip.close
```

## Alternative way
```python
from zipfile import ZipFile
# we can also use `with` statement for zip operations

with ZipFile('files.zip', 'w') as zipp:
    for file in Path("ecommerce").rglob("*"): # this will return a generator object which will iterate over all the files in the directory
        zipp.write(file) # this will add the file to the zip file

# rglob will return all the files in the directory and subdirectories ( using * will return all the files( including directories) in the directory and subdirectories
#  using *.* will return all the files in the directory and subdirectories with the extension)

```
* In above code we are using `with` statement to open the zip file. This will automatically close the zip file after the operation is done.


## Listing all files of a zip file

```python
from zipfile import ZipFile

path = Path() / "files.zip"


# we can also print the files in the zip file
with ZipFile(path) as zipp:
    print(zipp.namelist())   # this will print all the files in the zip file
```

* In Above code we are using `with` statement to open the zip file. This will automatically close the zip file after the operation is done.
* for path we are using `Path()` to get the path of the file. This is because we are using `Path` module to get the path of the file. We can also use `Path` module to get the path of the file.

## Extracting files from a zip file

```python
from zipfile import ZipFile
# we can also extract the files from the zip file

with ZipFile(path) as zipp:
    zipp.extractall("extracted") # this will extract all the files in the zip file to the extracted folder
```


Overall, zip files are very useful to compress files and send them over the internet. We can also use zip files to send multiple files in a single file.

