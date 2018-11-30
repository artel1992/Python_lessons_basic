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
#
# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import argparse
import sys
import hw05_easy
import re


def get_command(command=0,error=False):
    if command==0 and not error:
            command = input("1. Перейти в папку\n"+
                            "2. Просмотреть содержимое текущей папки\n"+
                            "3. Удалить папку\n"+
                            "4. Создать папку\n")
            try:
                command= int (command)
            except ValueError:
                    get_command(command=0,error=True)
    elif command >= 1 and command <=4 and not error:
        return int(command)
    else:
        print("Команда введена не верно, повторите попытку: ")
        command=input("1. Перейти в папку\n" +
                          "2. Просмотреть содержимое текущей папки\n" +
                          "3. Удалить папку\n" +
                          "4. Создать папку\n")
        try:
            command= int (command)
        except ValueError:
            get_command(command=0,error=True)
    return command

def util(command,name:str = None,count:int = 1):
    if command==1:
        pass
    elif command==2:
        return hw05_easy.get_thisDir()
    elif command==3:
        pass
    elif command==4:
        if name == None:
            name = input('Введите имя')
        count = input('и количество(необязтельно)')
        result = hw05_easy.addDir(name,count)
        if result:
            return result
        else:
            print('Количество введено не верно, пожалуйста повторите попытку')
            util(command,name)
command =get_command()
print(util(command))
