# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.

import re

'''
Первый способ
'''
s = 'mtMmEZUOmcqGKGBJMjhjhkHjnHkjhKJhKJFFHGF'
pattern1 = r'[A-Z]+([a-z]+)'
pattern2 = r'([a-z]+)[A-Z]+'
found = list(set(re.findall(pattern1, s) + re.findall(pattern2, s)))
print(found)

'''
Второй способ //надо доделать
'''
s = 'mtMmEZUOmcqGKGBJMjhjhkHjnHkjhKJhKJFFHGF'

print('====================================')

# Задание-2:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.

import random

def fill_fail(fail_name):
    '''
    Заполнение файла цифрами
    '''
    f = open(fail_name, 'w')
    for i in range(2500):
        f.write(str(random.randint(0,9)))
    f.close()

fill_fail('1.txt')
f = str(open('1.txt').readlines())
'''
потом доделаю
'''
print('====================================')


