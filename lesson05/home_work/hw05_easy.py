# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
from shutil import copyfile
def addDir(name='dir',count=1):#Добавление лирикторий
    try:
        count=int(count)#Попытка приобразовать строку в число
    except ValueError:#Если неудачно то возвращаем ложь
        return False
    dir_names = []#список с именами дирикторий
    if count>1:#если не 1 папка
        for i in range(1,count+1):
            try:
                os.mkdir(f"{name}_{i}")
            except FileExistsError:# Если папка существует пропускаем итерацию
                continue
            dir_names.append(f"{name}_{i}")

    else:#Если 1 директория
        try:
            os.mkdir(f"{name}")
        except FileExistsError:#Если директория существует вернуть ошибку
            return 'Данная директория существует'

    if dir_names.__len__()==0:#если список с именами дирикторий пуст то
        return f'Папка {name} создана'
    else:# если он не пуст то объединяем имена и возвращаем
        dir_names = ' , '.join(dir_names)
        return f'Папки {dir_names} созданы'

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
def get_thisDir():
    result = []
    for path in os.listdir(os.getcwd()):#Перебераем все содержимое текущей папки
        if os.path.isdir(path):#Если дириктория
            result.append(f'Папка:{path}')
        elif os.path.isfile(path):# если файл
            result.append(f'Файл:{path}')
    result ='\n'.join(result)# объединяем всё в одну строку
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