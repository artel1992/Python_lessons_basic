import re
# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
def get_K(str:equation):
    k= re.search('[-\s](\d+)x',equation)
    k=equation[k.span()[0]:k.span()[1]]
    k=k.replace("x",'')
    if k[0]=="-":
        return int(k)
    else:
        k = k.replace(" ", '')
        return int(k)
def get_B(str:equation):
    if re.search("\+",equation):
        b = equation.split('+')
    else:
        b = equation.split('-')
        b[len(b) - 1] =b[len(b) - 1].replace(" ","")
        b[len(b) - 1]="-"+b[len(b) - 1]
    b = float(b[len(b) - 1])
    return b
b = get_B(equation)
k=get_K(equation)
y = k*x + b
# вычислите и выведите y


# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'
# date=input('Date:')

# Примеры некорректных дат
# date = '01.22.1001'
# date = '1.12.1001'
# date = '-2.10.3001'
def date_corect(date_string):
    date = date_string.split(".")
    if date.__len__()==3:
        day = date[0]
        month = date[1]
        max_day=30
        yaer = date[2]
    else:
        day = "01"
        month = "01"
        yaer= "0001"
    if  month.__len__()>=3:
        month = month[0]+month[1]
    elif month.__len__()==0:
         month = "01"
    if int(month)>12 :
        month="12"
    elif int(month)<1:
        month="01"
    if int(month)<=7 and int(month)%2==0:
        max_day = 30
    elif int(month)<=7 and int(month)%2!=0:
        max_day =31
    elif int(month )> 7 and int(month) % 2 == 0:
        max_day =31
    elif int(month )> 7 and int(month)%2!=0:
        max_day = 30
    if  day.__len__()>=3:
        day = day[0]+day[1]
    elif day.__len__()==0:
         day = "01"
    if int(day) > max_day:
        day="{max_day}".format(max_day=max_day)
    elif int(day)< 1:
        day="01"
    if  yaer.__len__()>=5:
        yaer = yaer[0]+yaer[1]+yaer[2]+yaer[3]
    elif yaer.__len__()==0:
         yaer = "0001"
    elif yaer.__len__() < 4:
        yaer= "0"*(4-yaer.__len__())+yaer
    if int(yaer)>9999:
        year="9999"
    elif int(yaer)<1:
        year="0001"
    return day+"."+month+"."+yaer
print(date_corect(date))
# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3
def bashnya(count):
    a=1
    i=2
    b=count
    e=1
    c=0
    while b>a:
        n = 1
        a+=i*i
        e+=i
        c=a-b
        test=(a-i*i)+1
        z=(e-i)+1
        while n<=i:
            if test!=b:
                test+=1
                n += 1
                if n==i and test!=b:
                    z+=1
                    n=0
            if test==b:
                break
        i += 1
    return z,n
print(bashnya(19))
