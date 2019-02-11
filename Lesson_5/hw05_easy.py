# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create_dirs():
    '''
    Создает директории в текущей папке
    '''
    for i in range(1,10):
        try:
            os.mkdir(os.path.join(os.getcwd(), 'dir_' + str(i)))
        except FileExistsError:
            print('Already exists!')

def delete_dirs():
    '''
    Удаляет директории в текущей папке
    '''
    for i in range(1,10):
        try:
            os.rmdir(os.path.join(os.getcwd(), 'dir_' + str(i)))
        except FileNotFoundError:
            print('Already doesn\'t exist!')

create_dirs()
delete_dirs()

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#ТОЛЬКО ПАПКИ, А НЕ ФАЙЛЫ!

list = [print(i) for i in os.listdir(os.getcwd()) if os.path.isdir(os.path.join('.', i))]

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# ИСПОЛЬЗОВАТЬ ТОЛЬКО МОДУЛЬ OS

try:
    os.link(os.path.join(os.getcwd(), os.path.basename(__file__)), os.path.join(os.getcwd(), str('copy_' + os.path.basename(__file__))))
except FileExistsError:
    print('Already exists!')


#функции для задания нормал
def print_help():
    print('Выберите необходимое действие: ')
    print('1. Перейти в папку')
    print('2. Просмотреть содержимое текущей папки')
    print('3. Удалить папку')
    print('4. Создать папку')

def create_dir(dir_name):
    try:
        os.mkdir(os.path.join('.', dir_name))
        print('Успешно создано')
    except FileExistsError:
        print('Невозможно создать')

def delete_dir(dir_name):
    try:
        os.rmdir(os.path.join('.', dir_name))
        print('Успешно удалено')
    except FileNotFoundError:
        print('Невозможно удалить')

def change_dir(dir_name):
    try:
        os.chdir(os.path.join('.', dir_name))
        print('Успешно перешел')
    except FileNotFoundError:
            print('Невозможно перейти')



