# read line method


# myfile = open("file.txt", "r",encoding = "UTF-8")

# print(myfile.readline()) # read the first line
# print(myfile.readline()) # read the second line
# print(myfile.readline()) # read the third line
# myfile.close()

# we can use it with loop also.
# If you use readline(), you need to explicitly call it within a loop until the end of the file is reached.

# while True:
#     line = myfile.readline()
#     if not line:
#         break
#     print(line)
# myfile.close()



# reding line from txt file using for loop 

# with open("file.txt","r",encoding = "UTF-8") as myfile2:
#     for lines in myfile2:
#         print(lines)



# writelines() method 

# with open("file.txt",'a',encoding='utf-8') as myfile3:  # a tag for appending a new line
#     myfile3.writelines("\nhey this is amazing")

# similarly you can write or append characters as well at the end of the line. You can also pass a list of lines to the writelines() arguments
with open("file.txt",'a',encoding='utf-8') as myfile3:  # a tag for appending a new line
    lines = ["Python is a great language", "Learning is fun", "consistency is the key"]

    for index,i in enumerate(lines):
        lines[index] = "\n" + lines[index]  # updating contents of list by adding a newline character in front of every list item.

    myfile3.writelines(lines)  # writing lines from list
