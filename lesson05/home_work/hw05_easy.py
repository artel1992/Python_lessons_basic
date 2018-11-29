# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
from shutil import copyfile
def addDir(name='dir',count=1):
    count=int(count)
    dir_names = []
    if count>1:
        for i in range(1,count+1):
            try:
                os.mkdir(f"{name}_{i}")
            except FileExistsError:
                if len(os.listdir(f"{name}_{i}")) == 0:
                    continue
            dir_names.append(f"{name}_{i}")
                   # os.rmdir(f"{name}_{i}")

    else:
        try:
            os.mkdir(f"{name}")
        except FileExistsError:
            return 'Данная папка существует'

    if dir_names.__len__()==0:
        return f'Папка {name} создана'
    else:
        dir_names = ' , '.join(dir_names)
        return f'Папки {dir_names} созданы'

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def get_thisDir():
    result = []
    for path in os.listdir(os.getcwd()):
        if os.path.isdir(path):
            result.append(f'Папка:{path}')
        elif os.path.isfile(path):
            result.append(f'Файл:{path}')
    result ='\n'.join(result)
    return result
# # Задача-3:
# # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# copy_file = "copy.py"
# if not os.path.exists(copy_file):
#     copyfile(os.path.basename(__file__),copy_file)
# else:
#      for path in os.listdir(os.getcwd()):
#          if os.path.isfile(path=path):
#              if os.path.split(path)[1]==copy_file:
                 #os.remove(path)