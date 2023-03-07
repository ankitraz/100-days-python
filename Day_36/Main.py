import os

# f = os.open("D:\\my_workspace\\100_days_python\\Day_36\\details.txt", os.O_RDONLY)
# contents = os.read(f,4000)
# print(contents)
# os.close(f)

# f2 = os.open("D:\\my_workspace\\100_days_python\\Day_36\\details.txt", os.O_WRONLY)

# # Write to the file
# os.write(f2, b"this is another line")

# os.close(f2)

# list all the folder in current directory
# files = os.listdir(".")
# print(files)


# create a directory 
# os.mkdir("newdir")

# remove a directory
# os.rmdir("newdir")


#create a new file or create multiple files-
for i in range(5):
    file = open(f"file_{i}.txt","x")
