# Задача-1:
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
'''
import sys
import os

while True:
    print('Выберите необходимое действие: ')
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')
    key = int(input(''))
    if key == 1:
        folder_name = input('Введите название папки:')
        try:
            os.chdir(os.path.join('.', folder_name))
            print('Успешно перешел')
        except FileNotFoundError:
            print('Невозможно перейти')
    if key == 2:
        print(os.listdir())
    if key == 3:
        folder_name = input('Введите название папки:')
        try:
            os.rmdir(os.path.join('.', folder_name))
            print('Успешно удалено')
        except FileNotFoundError:
            print('Невозможно удалить')
    if key == 4:
        folder_name = input('Введите название папки:')
        try:
            os.mkdir(os.path.join('.', folder_name))
            print('Успешно создано')
        except FileExistsError:
            print('Невозможно создать')

'''

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
# ИСПОЛЬЗОВАТЬ МОДУЛЬ OS и SHUTIL

import hw05_easy as m
import os

while True:
    m.print_help()
    key = int(input())
    if key == 1 or key == 3 or key == 4:
        folder_name = input('Введите название папки:')
        if key == 1:
            m.change_dir(folder_name)
        if key == 3:
            m.delete_dir(folder_name)
        if key == 4:
            m.create_dir(folder_name)
    elif key == 2:
        print(os.listdir())
    else:
        print('Такой команды не сущестует')








