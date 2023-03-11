marks = [12,4,68,7,9]


# index = 0
# for i in marks:
#     print(i)
#     if ( index == 3):
#         print("Topper")
#     index += 1      



for index, i in enumerate(marks):  # we can also change the start value
    print(i)
    if index == 3:
        print("pro")


# the enumerate function is a built in function in python that allows you to loop over a sequence 
# such as list, tuple or string) and get the index and value of each element in the sequence at the same time.
