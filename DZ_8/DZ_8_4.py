# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках
# реализовать параметры, уникальные для каждого типа оргтехники.


class Store:
    def __init__(self, items = None):
        if not items:
            items[]
        self.items = items

    def add_items(self, item):
        self.items.append(item)

    def get_items(self, item):
        if item in self.items:
            self.items.remove(item)
        else:
            print('Этой техники нет')


class Equipment:
    def __init__(self, name):
        self.name = name

class Printer(Equipment):
    def __init__(self, name):
        super(Printer, self).__init__(name)
        self.group = 'Printer'


class Scanner(Equipment):
    def __init__(self, name):
        super(Scanner, self).__init__(name)
        self.group = 'Scanner'

class Copier(Equipment):
    def __init__(self, name):
        super(Copier, self).__init__(name)
        self.group = 'Printer'