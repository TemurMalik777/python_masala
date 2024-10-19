import os

dir_papka = r'D:\Men_bekorchiman'
folder_count = 0

if os.path.exists(dir_papka):
    for item in os.listdir(dir_papka):
        item_path = os.path.join(dir_papka, item)
        if os.path.isdir(item_path):
            folder_count += 1

print(f"{dir_papka} papkasida {folder_count} ta papka bor.")