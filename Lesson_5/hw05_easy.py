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
'''
os.link(тут путь до текущего файла, os.getcwd()))
'''