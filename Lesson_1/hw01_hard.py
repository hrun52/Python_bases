
__author__ = 'Поплавская Варвара Антоновна'

# Задание-1:
# Ваня набрал несколько операций в интерпретаторе и получал результаты:
# 	Код: a == a**2
# 	Результат: True
# 	Код: a == a*2
# 	Результат: True
# 	Код: a > 999999
# 	Результат: True

# Вопрос: Чему была равна переменная a,
# если точно известно, что её значение не изменялось?


import math

a = math.inf

if a == a**2 and a == a*2 and a > 999999:
    print('Значение а: ', a)
else:
    print('Чему тогда равно а? ¯\_(ツ)_/¯')