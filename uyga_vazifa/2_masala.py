import os

for i in range(4):
    path = os.path.join(r"D:\Men_bekorchiman", f"{i}_file")
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print(f"Katalog allaqachon mavjud: {path}")
