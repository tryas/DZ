#  Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#  Значения данных атрибутов должны передаваться при создании экземпляра класса.
#  Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
#  для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
#  для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна.
#  Проверить работу метода.



class Road:
    def __init__(self):
        massa_one_meter = 15
        _road_lenght = 0
        _road_width = 0
        road_thickness = 1


    def massa(self, road_lenght, road_width, road_thickness):
        plochad = int(road_lenght) * int(road_width)
        massa = plochad * road_thickness * 15
        print('Масса дорожного полотна =', massa , 'кг')


my_road_1 = Road()
my_road_1.massa(10, 1000, 3)
my_road_2 = Road()
my_road_2.massa(10, 1000, 6)
