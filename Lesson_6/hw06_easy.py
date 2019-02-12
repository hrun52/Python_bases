'''
Задача-1: Написать класс, например, Worker, который должен содержать информацию
о работнике (ФИО, оклад, надбавка за напряженность).
Создать экземпляр класса и передать конкретные данные (примеры ФИО, должности,
оклад и надбавки). Оклад и надбавку передать в виде строки.
На основе строки создать атрибут income, который реализовать в виде словаря
и инкапуслировать. Словарь income должен содержать информацию об окладе и надбавке.
Применить к экземпляру
класса метод __dict__ и проверить какой будет результат применения этого метода.
А комментариях к заданию написать тип результата на русском языке.
'''

class Worker:
    #Функция-конструктор класса
    def __init__(self, name, surname, position, salary, premium, age):
        #атрибуты класса
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.premium = premium
        self.age = age

        self.__income = {
        'salary': int(salary),
        'premium': int(premium)
        }

    #метод вывода полного имени и возраста сотрудника
    def get_fullname_and_age(self):
        return f'Полное имя: {self.name} {self.surname}. Возраст: {self.age}'


#создание экземпляра класса
worker_1 = Worker('Bob', 'Smith', 'CTO', '12345', '6789', '30')
worker_1.__dict__
#print(worker_1.__income)

'''
Задача-2: Продолжить работу над задачей 1. Создать на основе класса Worker класс
Position (реализовать наследование). Добавить классу уникальный атрибут -
% премии к зарплате (от суммы оклада).
Создать метод расчета зарплаты с учетом только премии.
Реализовать обращение к этому атриубуту, как к свойству.
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

class Position(Worker):
    def __init__(self, name, surname, position, salary, premium, age, percentage):
        #явный вызов конструктора класса-родителя
        Worker.__init__(self, name, surname, position, salary, premium, age)
        self.percentage = percentage

    @property
    def calc_salary(self):
        return int(self.salary) + int(self.salary) * int(self.percentage) / 100

    def calc_income(self):
        return int(self.salary) + int(self.salary) * int(self.percentage) / 100 + int(self.premium)

pos_1 = Position('Bob', 'Smith', 'CTO', '10000', '1000', '30', '10')
print(pos_1.calc_salary)
print(pos_1.name, pos_1.surname, pos_1.position, pos_1.salary, pos_1.premium, pos_1.percentage)

'''
Задача-3: Продолжить работу над задачей 2.  Реализовать полиморфизм
использования знака + в методах 1) вывода полного имени работника и возраста
2) вычисления общего дохода работника с учетом надбавки .
Проверить работу всей структуры на реальных данных, вывести результаты.
'''

print(worker_1.get_fullname_and_age())
print(pos_1.calc_income())


