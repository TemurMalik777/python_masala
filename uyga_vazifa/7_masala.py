import os

dir_file = r'D:\Men_bekorchiman'
file_count = 0

if os.path.exists(dir_file):
    for item in os.listdir(dir_file):
        item_path = os.path.join(dir_file, item)
        if os.path.isfile(item_path):
            file_count += 1

print(f"{dir_file} papkasida {file_count} ta fayl bor.")