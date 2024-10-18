import os
my_cwd = os.getcwd()
result = os.walk(my_cwd)
for i, j, k in result:
    for file in k:
        print(i, ' - ', file)
print(j)