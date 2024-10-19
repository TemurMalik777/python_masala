import os
import shutil

my_cwd = os.getcwd()
new_dir = (r'D:\Koppiy')
path = os.path.join(my_cwd, new_dir)
os.mkdir(path)
print(os.listdir())


put_dir = r'D:\Sen_bekorchisan'
kop_dir = r'D:\Koppiy\Sen_bekorchiman'

if not os.path.exists(put_dir):
    print(f"Manba katalogi topilmadi: {put_dir}")
else:
    if not os.path.exists(os.path.dirname(kop_dir)):
        os.makedirs(os.path.dirname(kop_dir))
 
    try:
        shutil.copytree(put_dir, kop_dir, dirs_exist_ok=True)
        print(f"Katalog nushalandi: {kop_dir}")
    except Exception as e:
        print(f"Katalog nushalashda xato: {e}")