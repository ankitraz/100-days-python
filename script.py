# Script to rename folders in a directory
import os

l = []
with open('names.txt', 'r',encoding='utf') as f:
    lines = f.readlines()
    
    for line in lines:
        l.append(line.strip())  # strip removes the newline character or any other character from the end of the string

# print(l)
for index, i in enumerate(l):
    if index <= 9:
        old_folder_path = os.path.join("D:\\", "my_workspace", "100_days_python", f"Day_0{index}")
        new_folder_path = os.path.join("D:\\", "my_workspace", "100_days_python", f"Day_0{index}_{i}")
    else:
        old_folder_path = os.path.join("D:\\", "my_workspace", "100_days_python", f"Day_{index}")
        new_folder_path = os.path.join("D:\\", "my_workspace", "100_days_python", f"Day_{index}_{i}")

    if not os.path.exists(new_folder_path):
        os.rename(old_folder_path, new_folder_path)
