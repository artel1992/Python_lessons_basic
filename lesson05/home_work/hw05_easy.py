# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
from shutil import copyfile
for i in range(1,10):
    try:
        os.mkdir(f"dir_{i}")
    except FileExistsError:
        #print(f"Error: dir{i} already exist")
        if len(os.listdir(f"dir_{i}")) == 0:
            os.rmdir(f"dir_{i}")
            #print("123")
#os.removedirs(path)
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        print(path)
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
copy_file = "copy.py"
if not os.path.exists(copy_file):
    copyfile(os.path.basename(__file__),copy_file)
else:
     for path in os.listdir(os.getcwd()):
         if os.path.isfile(path=path):
             if os.path.split(path)[1]==copy_file:
                 os.remove(path)