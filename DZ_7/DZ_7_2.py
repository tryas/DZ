# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
# название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.



from abc import ABC, abstractmethod

class Odejda(ABC):
    @abstractmethod
    def raschod(self):
        pass

class Palto(Odejda):
    def __init__(self, razmer):
        self.razmer = razmer

    @property
    def raschod(self):
        return((self.razmer / 6.5) +0.5)

class Costum(Odejda):
    def __init__(self, rost):
        self.rost = rost

    @property
    def raschod(self):
        return((self.rost * 2 + 0.3))

palto = Palto(48)
costum = Costum(1.78)
print(palto.raschod)
print(costum.raschod)
print('Obchij raschod = ', palto.raschod + costum.raschod)