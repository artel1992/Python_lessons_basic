# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import argparse
import os
import sys
import shutil
#print('sys.argv = ', sys.argv[1:])
# Получаем аргументы команды
def get_arg():
    pars = argparse.ArgumentParser()
    pars.add_argument('-m','--mkdir',help="mkdir <dir_name> - создание директории")
    pars.add_argument('-cp','--copy', help="cp <file_name> - копия указанного файла",type=open)
    pars.add_argument('-rm','--remove', help="rm <file_name> - удалить указанный файл",type=open)
    pars.add_argument('-cd', help="cd <full_path or relative_path> - смена дириктории на указанную")
    pars.add_argument('-ls',nargs='?',help="ls - отобразить полный путь текущей директории")
    pars.add_argument('-ping', help="ping - тестовый ключ")
    return pars.parse_args(sys.argv[1:])

arguments = get_arg()
# Создание директории
def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))

# Копируем файл из текущей папки в папку copy_files
def copy_file(file_name:str):
    path = os.getcwd()#Текущий путь
    listdir = os.listdir(path)#Смотрим существует ли нужная папка
    if 'copy_files' in listdir:#Если да то просто копируем в нее
        try:
            shutil.copy2(os.path.join(path,file_name),os.path.join(path,'copy_files'))
        except FileNotFoundError:
            print('Файл не найден')
            return 0
    else:#Иначе создаем потом копируем
        dir_name='copy_files'
        make_dir(dir_name)
        try:
            shutil.copy2(os.path.join(path,file_name),os.path.join(path,'copy_files'))
        except FileNotFoundError:
            print('Файл не найден')
            return 0
    path = os.path.join(path,'copy_files',file_name)
    return path

#Удаляем файл или дирикторию
def remove(path:str):
    if os.path.exists(path):#Прверяем существует ли данный файл/дириктория
        if os.path.isfile(path):#Если да то проверяем файл ли это
            os.remove(path)
        if os.path.isdir(path):#или дириктория
            shutil.rmtree(path)
        if os.path.exists(path):#Если после удаления путь существует значит по каким то причинам удаление не произошло
            return 'Неудаленно ошибка не известна'
        return f'{path} Успешно удален '
    else:
        return "Файл не найден"


# Если есть аргумент то выполняем его функцию
if arguments.mkdir:
    make_dir(arguments.mkdir)
if arguments.copy:
    print('Файл успешно скопирован в: '+copy_file(arguments.copy.name))
if arguments.remove:
    print(remove(arguments.remove.name))
if arguments.cd:
    print(os.chdir(os.path.join(os.getcwd(),arguments.cd)))#Смысл от этого я не понял оди фиг файл закрывается и толком не понятно сменилась дириктория или нет
    print(f'Текущая дириктория : {os.getcwd()}')
    #input()
if '-ls' in sys.argv[1:]:
    print(os.getcwd())
