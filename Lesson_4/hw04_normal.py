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

print(re.findall('[a-z]+', s))

'''
Второй способ
'''
s = 'mtMmEZUOmcqGKGBJMjhjhkHjnHkjhKJhKJFFHGF'
board1 = 0
board2 = 0
i = 0
result = []
while i < len(s):
    if s[i].isupper():
        board1 = board2
        board2 = i
        result.append(s[board1:board2])
        while i < len(s) and s[i].isupper():
            i += 1
            board2 = i
    i += 1
print(result)

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
    for i in range(25000):
        f.write(str(random.randint(0,9)))
    f.close()

fill_fail('1.txt')
f = str(open('1.txt').readlines())
max_len = 1
max_seq = []
i = 0
while i < len(f):
    temp_max_len = 1
    while i + 1 < len(f) and f[i + 1] == f[i]:
        temp_max_len += 1
        i += 1
        if max_len < temp_max_len:
            max_len = temp_max_len
            max_seq = f[i - max_len + 1 : i + 1]
    if temp_max_len == 1:
        i += 1

print(max_len, max_seq)

print(max(re.findall(r'0+|1+|2+|3+|4+|5+|6+|7+|8+|9+', f), key = len)) #посмотрела в видеоуроке, что можно было в тыщу раз проще сделать

print('====================================')


