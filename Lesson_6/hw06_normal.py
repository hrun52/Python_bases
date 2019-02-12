'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''
import math

class Triangle():
    def __init__(self, x1, x2, x3, y1, y2, y3):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def calc_area(self):
        return 0.5 * math.fabs((self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3))

    def calc_perimeter(self):
        first_side = ((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)**0.5
        second_side = ((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)**0.5
        third_side = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        return first_side + second_side + third_side


figure = Triangle(1, 2, -8, 3, -5, 4)
print(figure.calc_area())
print(figure.calc_perimeter())