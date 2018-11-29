## Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import argparse
import sys
import hw05_easy


def get_arg():
    pars = argparse.ArgumentParser()
    pars.add_argument('-u','--util',default='1')
    return pars

def get_command(command=0):
    a = get_arg()
    a = a.parse_args(sys.argv[1:])
    if command==0:
        if a.util:
            command = int(input("1. Перейти в папку\n"+
                            "2. Просмотреть содержимое текущей папки\n"+
                            "3. Удалить папку\n"+
                            "4. Создать папку\n"))
            if command=='':
                get_command(command=0)
    elif command >= 1 and command <=4:
        return int(command)
    else:
        command=int(input("Команда введена не верно, повторите попытку: \n"+
                                "1. Перейти в папку\n" +
                                "2. Просмотреть содержимое текущей папки\n" +
                                "3. Удалить папку\n" +
                                "4. Создать папку\n"))
        if command == '':
            get_command(command=0)
    return command


def util(command):

    if command==1:
        pass
    elif command==2:
        return hw05_easy.get_thisDir()
    elif command==3:
        pass
    elif command==4:
        name = input('Введите имя')
        count = input('и количество(необязтельно)')
        if count=='':
            count=1
        if name == '':
            util(command)
        return hw05_easy.addDir(name,count)
command =get_command()
print(util(command))