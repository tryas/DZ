# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.

import company


class Store:
    def __init__(self):
        self.items = dict()

    def add_items(self, item):
        try:
            self.items[item.to_str()] = self.items[item.to_str()] + 1
        except KeyError:
            self.items[item.to_str()] = 1

    def get_items(self, item):
        try:
            self.items[item.to_str()] = self.items[item.to_str()] - 1
            if self.items[item.to_str()] == 0:
                self.items.pop(item.to_str())
        except KeyError:
            print('Этой техники нет')

    def from_store_to_depart(self, depart, item):
        self.get_items(item)
        try:
            depart.items[item.to_str] = depart.items[item.to_str] + 1
        except KeyError:
            depart.items[item.to_str()] = 1


class Equipment:
    def __init__(self, name, year_of_production):
        self.name = name
        self.year_of_production = year_of_production


class Printer(Equipment):
    def __init__(self, name, model, year_of_production, color):
        super(Printer, self).__init__(name, year_of_production)
        self.group = 'Printer'
        self.model = model
        self.year_of_production = year_of_production
        self.color = color

    def equals(self, another):
        if self.name == another.name and self.model == another.model \
                and self.year_of_production == another.year_of_production \
                and self.color == another.color:
            return True
        else:
            return False

    def to_str(self):
        return self.group + ' ' + self.name + ' ' + self.model + ' ' + str(self.year_of_production) + ' ' + self.color


class Scanner(Equipment):
    def __init__(self, name, model, year_of_production, color_depth):
        super(Scanner, self).__init__(name, year_of_production)
        self.group = 'Scanner'
        self.color_depth = color_depth
        self.model = model


class Copier(Equipment):
    def __init__(self, name, model, year_of_production, document_feeder):
        super(Copier, self).__init__(name, year_of_production)
        self.group = 'Printer'
        self.document_feeder = document_feeder
        self.model = model


my_printer = Printer('EPSON', 'EX-300', 2010, 'black')
print(my_printer.group)
print(my_printer.year_of_production)
print(my_printer.color)

my_scanner = Scanner('Xerox', 'BN340', 2020, 16)
print(my_scanner.model)

my_copier = Copier('Canon', 'Sa098', 2019, True)
print(my_copier.name)
print(my_copier.document_feeder)

my_store = Store()
my_store.add_items(my_printer)
new_printer = Printer('EPSON', 'EX-300', 2010, 'black')
my_store.add_items(new_printer)
new_printer1 = Printer('RICOH', 'EX-300', 2010, 'black')
my_store.add_items(new_printer1)
print(my_store.items)
# my_store.get_items(my_printer)
# print(my_store.items)

my_depart = company.Department1('Samsung', 'Seller')
my_store.from_store_to_depart(my_depart, new_printer)
print(my_store.items)
print(my_depart.items)
my_depart.from_depart_to_store(my_store, my_printer)
print(my_store.items)
print(my_depart.items)
