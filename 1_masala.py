import os 
print(os.getcwd())
print(os.listdir())
for x in os.listdir('..'):
    print(x)