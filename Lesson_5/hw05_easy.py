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

current_fail_path = os.path.join(os.getcwd(), os.path.basename(__file__))
#s.link('C:\\Users\\В.А.Поплавская\\Desktop\\1.txt', 'C:\\test\\1.txt')
#f = os.open(current_fail_path, os.O_RDWR|os.O_CREAT)
#os.close(f)
#dst = 'E:\\hw05_easy.py'
#os.link(current_fail_path, dst)
#os.link(current_fail_path, os.path.join(current_fail_path, ' - copy'))
print(os.path.join(os.getcwd(), os.path.basename(__file__)))

os.link(os.path.join(os.getcwd(), os.path.basename(__file__)), os.path.join(os.getcwd(), str('copy_' + os.path.basename(__file__))))

