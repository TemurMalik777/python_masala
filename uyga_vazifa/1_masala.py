import os

# my_cwd = os.getcwd()
# new_dir = (r'D:\Koppiy')
# path = os.path.join(my_cwd, new_dir)
# os.mkdir(path)
# print(os.listdir())


# for i in range(4):
#     path=os.path.join(r"D:\Men_bekorchiman",f"{i}_file")
#     os.mkdir(path)


new_dir = r'D:\Men_bekorchiman'
if not os.path.exists(new_dir):
    os.mkdir(new_dir)

print(os.listdir(new_dir))