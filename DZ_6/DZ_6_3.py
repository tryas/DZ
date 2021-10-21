#  Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#  name, surname, position (должность), income (доход). Последний атрибут должен
#  быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
#  например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
#  на базе класса Worker. В классе Position реализовать методы получения полного
#  имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position,
#  передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name = ''
    surname = ''
    position = ''
    wage = 0
    bonus = 0
    _income = {"wage": wage, "bonus": bonus}
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus" : bonus}



class Position(Worker):

#    full_name = ' '
#    total_salary = ' '


    def get_full_name(self):
        return (self.name, self.surname)

    def get_total_income(self):
        self.total_salary = self._income["wage"] + self._income["bonus"]
        return self.total_salary




radeev = Position('dima', 'radeev', 'student', 10_000, 20_000)
print(radeev.name)
print(radeev.surname)
print(radeev._income)
print(radeev.get_full_name())
print(radeev.get_total_income())