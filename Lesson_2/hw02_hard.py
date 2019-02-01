# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y
# например, equation = 'y = -12x + 11111140.2121'
"""
equat = 'y = 5x + 6'.split()
for i in equat:
    if i.find('x') != -1:
        k = int(i[:-1])
    if i.isdigit():
        b = int(i)
x = int(input('y = 5x + 6. Введите координату х: '))
print('y =', k * x + b)
"""
def summ(a = 10, b = 7):
    c = a + b
    return c
print(summ(10))
