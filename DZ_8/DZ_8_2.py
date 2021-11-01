#  Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#  Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
#  нуля в качестве делителя программа должна корректно обработать эту ситуацию и
#  не завершиться с ошибкой.


class Divide_zero(Exception):
    def __init__(self, txt):
        self.txt = txt
delimoe = input('Введите делимое :')
delitel = input('Введите делитель :')

try:
    delimoe = int(delimoe)
    delitel = int(delitel)
    if delitel == 0:
        raise Divide_zero('Деление на ноль !')
except ValueError:
    print('Вы ввели не число ')
except Divide_zero as err:
    print(err)
else:
    print('Результат =', delimoe / delitel)


