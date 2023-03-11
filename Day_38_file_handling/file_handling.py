# file handling is used to read and write data to a file


# write and create a file or opening a file
# var1 = open("file.txt", "w") # r is for read, w is for write, a is for append, r+ is for read and write
# var1.write("Hello World") # write to the file
# var1.close() # close the file

# open a file
var1 = open("file.txt", "r")
print(var1)
# print(var1.read()) # read the file
var1.close()


# modes in file
# r - read
# w - write
# a - append
# r+ - read and write
# w+ - write and read
# a+ - append and read

# with statement - it will automatically close the file

# with open("file.txt", "r") as var1:
#     print(var1.read())

