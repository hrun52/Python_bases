# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math. Функция округления числа n до amount знаков

import random

def on_round(n, amount):
    '''
    '''
    n = n.split('.')
    n[1] = n[1][:amount + 1]
    print(n[1])
    if int(n[1][:amount]) < 5:
        n[1] =n[1][:amount]
    else:
        temp = int(n[1][:amount]) + 1
        n[1] = str(temp)
    print(n[1])
    return n

num = str(random.uniform(10,100))
print(num)
num = on_round(num, 3)
print(num)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def generate_ticket():
    '''
     Генерация номера билета
    '''
    num = ''
    for i in range(0,6):
        num += str(random.randrange(0,9))
    return num

def check_happy(t):
    '''
    Проверка на то, является ли билет счастливым
    '''
    t_list = list(t)
    t_list = [int(i) for i in t_list]
    for i in range(0, len(t_list)):
        t_list[i] = int(t_list[i])
    if t_list[0] + t_list[1] + t_list[2] == t_list[3] + t_list[4] + t_list[5]:
        return True
    else:
        return False

ticket = generate_ticket()

if check_happy(ticket):
    print(ticket, '- Билет счастливый!')
else:
    print(ticket, '- Не повезло:(')
