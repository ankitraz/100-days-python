# suppose we want to break for loop when a certain condition is met.
# we can break our loop whenever we want.

# num = [2,5,6,7,8,99]
# target = 0
# # the job is to find the target inside num list. when found the target simply break the loop and print the index of target element in the list.
# for i in num:
#     if i == target:
#         print("Target is present in the list.")
#         break
#     print("Target is not present in list.")
#     break




# # print a table
# for i in range(1,12):
#     if i == 11:
#         break
#     print("5 * ",i, " = ",5*i)




# using continue in for loop
sum = 0
for i in range(11):
    if i == 1 or i == 2 or i == 0:
        continue
    sum += i
print(sum)





