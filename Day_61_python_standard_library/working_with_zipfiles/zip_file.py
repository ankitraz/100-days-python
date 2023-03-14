from pathlib import Path
from zipfile import ZipFile

# first create an object of zip file

# zip = ZipFile('files.zip', 'w') # w is for write mode

# # add files to the zip file

# iterator = Path("ecommerce").rglob("*.*") # this will return a generator object which will iterate over all the files in the directory

# for file in iterator:
#     zip.write(file) # this will add the file to the zip file
# zip.close



#=======================================================================================================
# we can also use `with` statement for zip operations

with ZipFile('files.zip', 'w') as zipp:
    for file in Path("ecommerce").rglob("*"): # this will return a generator object which will iterate over all the files in the directory
        zipp.write(file) # this will add the file to the zip file

# rglob will return all the files in the directory and subdirectories ( using * will return all the files( including directories) in the directory and subdirectories
#  using *.* will return all the files in the directory and subdirectories with the extension)

path = Path() / "files.zip"


# we can also print the files in the zip file
with ZipFile(path) as zipp:
    print(zipp.namelist())   # this will print all the files in the zip file


# we can also extract the files from the zip file

with ZipFile(path) as zipp:
    zipp.extractall("extracted") # this will extract all the files in the zip file to the extracted folder
