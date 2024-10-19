import os

new_dir = r'D:\Sen_bekorchisan'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

print(os.listdir(new_dir))

for i in range(4):
    path=os.path.join(r"D:\Sen_bekorchisan",f"{i}_file")
    os.mkdir(path)
