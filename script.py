import os



l = []
with open('names.txt', 'r',encoding='utf') as f:
    lines = f.readlines()
    
    for line in lines:
        l.append(line.strip())

print(l)


# for index,i in enumerate(l):
#     os.rename(f"Day_0{index}","Day_0{index}_{i}")
#     if index > 9:
#         os.rename(f"Day_{index}","Day_{index}_{i}")

for i in l:
    old_folder_path = os.path.join("D:", "my_workspace", "100_days_python", f"Day_0{index}")
    new_folder_path = os.path.join("D:", "my_workspace", "100_days_python", f"Day_0{index}_{i}")
    if not os.path.exists(new_folder_path):
        os.rename(old_folder_path, new_folder_path)
