# we can also use else with for loop as well

for i in range(5):
    print(i)
else:
    print("No more i")


for i in "Ankit raj":
    print(i)
else:
    print("Name is over")


## very important
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("hello world") # this line won't get executed😂 because else only works when loop is finished(last iteration is processed) and not breaked in between in an iteration

