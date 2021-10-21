# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print('turn in direction : ', direction)

    def show_speed(self, speed):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print ('Speed limit 60 !')

class SportCar(Car):
    def show_speed(self):
        print(self.speed)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print ('Speed limit 40 !')

class PoliceCar(Car):
    def show_speed(self):
        print(self.speed)

mersedes = TownCar(120, 'black', 'SL', False)
mazerati = SportCar(200, 'red', 'GranTourismo', False)
hyandai = WorkCar(50, 'yellow', 'solaris', False)
chevrole = PoliceCar(150, 'white', 'express', True)

mersedes.show_speed()
hyandai.show_speed()
mazerati.show_speed()
chevrole.show_speed()
chevrole.turn('Right')


