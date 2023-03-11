# seek and tell function are used to work with file objects
# and their positions withing a file. these functions are part of the built-in io module.



# seek () function - it allows you to move the current position withing a file to a specific point.
# the position is specified in bytes, and you can move either forward or backward from the current position.

with open('file.txt','w+', encoding='utf') as f:  # w+ means write and read permission
    # move to the 10th byte in the file
    f.write("Hey this is ankit.")
    f.seek(4)


    # read the next  3 bytes after seeking 4 bytes
    data = f.read(3)
    print(data)


# tell() function is returns the current position within the file, in bytes.
with open('file.txt', 'r', encoding='utf') as f:
    # read the first 10 bytes
    data = f.read(10)

    # saves the current position
    current_position = f.tell()

    # Seek to the saved position
    print(f.seek(current_position))





# truncate() function - When you open a file in Python using the open function, you can specify the mode in which you want to open the file. If you specify the mode as 'w' or 'a',
#  the file is opened in write mode and you can write to the file. 
# However, if you want to truncate the file to a specific size, you can use the truncate function.
# The f.truncate(5) method call truncates the file to 5 bytes (or characters) in size, discarding any content after the first 5 bytes.

with open('file.txt', 'w', encoding='utf') as f:
    f.write("Hello world!")
    f.truncate(5)