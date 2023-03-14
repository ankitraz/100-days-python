# script to read all the directories in a given path and write them to a file

from pathlib import Path
import os


# path = Path(r"D:\my_workspace\100_days_python")

l = []

path = Path(r"D:\my_workspace\100_days_python")

for i in os.listdir(path=path):
    if os.path.isdir(i) and i != ".git" and i != "temp" and i != "quiz_app" and i != "myenv":
        l.append(i)

# print(l)

with open("new.txt",'a',encoding='utf') as f:
    for i in l:
        f.writelines("* "+ i + "\n")