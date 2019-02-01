# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    list = []
    list.append(1)
    list.append(1)
    for i in range(2, m + 1):
        list.append(list[i - 1] + list[i - 2])
    return list[n:m + 1]

n, m = map(int, input('Введите числа диапозона [n,m] через пробел:').split())
print(fibonacci(n - 1, m - 1))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

import random

def generate_sequence():
    '''
     Генерация последовательности
    '''
    seq = []
    for i in range(0,10):
        seq.append(random.randrange(0,100))
    return seq

def sort(list):
    '''
    Сортировка Хоара
    '''
    if len(list) <= 1:
        return list
    else:
        m = list[int(len(list)/2)]
        small = []
        equal = []
        big = []
        for i in list:
            if i < m:
                small.append(i)
            elif i == m:
                equal.append(i)
            else: big.append(i)
    return sort(small) + equal + sort(big)

list = generate_sequence()
print(sort(list))

#Задача-3:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

a1 = [1,5]
a2 = [2,1]
a3 = [7,1]
a4 = [6,5]
l = list(zip(a1,a2,a3,a4))
print(l)