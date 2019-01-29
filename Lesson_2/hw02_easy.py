# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:рандомный
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
# с помощью числа определяем ширину поля слева

fruits = ['apple', 'banana', 'kiwi', 'watermelon']
for fruit in fruits:
    print('{0}. {1:>10}'.format(fruits.index(str(fruit)) + 1, fruit))

print('====================================')

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

import random
a = random.sample(range(10), 5)
b = random.sample(range(10), 5)
print('a =', a, 'b =', b, 'answer =', set(a)-set(b))

print('====================================')
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

a = random.sample(range(10), 5)
result = []
for i in a:
    if i % 2 == 0:
        result.append(i / 4)
    else:
        result.append(i * 2)
print('a =', a, 'answer =', result)
