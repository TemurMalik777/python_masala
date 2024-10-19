import shutil
import os

papka_ochir = r'D:\Men_bekorchiman'

if os.path.exists(papka_ochir):
    shutil.rmtree(papka_ochir)
    print(f"Katalog o'chirildi: {papka_ochir}")
else:
    print(f"Katalog topilmadi: {papka_ochir}")