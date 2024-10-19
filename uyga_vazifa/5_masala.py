import os 
import shutil

fayil_ochir = r'D:\Men_bekorchiman'

if os.path.exists(fayil_ochir):
    for file_nomi in os.listdir(fayil_ochir):
        file_path = os.path.join(fayil_ochir, file_nomi)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"{file_path} ni o'chirishda xato: {e}")
else:
    print(f"Katalog topilmadi: {fayil_ochir}")
