# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный. В рамках метода
# реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.


from time import sleep
class TrafficLight:
    timing_red = 7
    timing_yellow = 2
    timing_green = 5
    colors = ['red', 'yellow', 'green']

    def __init__(self):
        self.color = 'green'
    def running(self):
        while True:
            for el in self.colors:
                if el == 'red':
                    print('red')
                    sleep(self.timing_red)
                else:
                    if el == 'yellow':
                        print('yellow')
                        sleep(self.timing_red)
                    else:
                        print('green')
                        sleep(self.timing_green)



my_trafficlight = TrafficLight()
my_trafficlight.running()
