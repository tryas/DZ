# Создайте собственный класс-исключение, который должен проверять содержимое списка
# на наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку
# типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.

class Proverka_spiska(Exception):
    def __init__(self, txt):
        self.txt = txt

# class OwnError(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
# inp_data = input("Введите положительное число: ")
#
# try:
#     inp_data = int(inp_data)
#     if inp_data < 0:
#         raise OwnError("Вы ввели отрицательное число!")
# except ValueError:
#     print("Вы ввели не число")
# except OwnError as err:
#     print(err)
# else:
#     print(f"Все хорошо. Ваше число: {inp_data}")
spisok = []
new_element = 0
while True:
        new_element = input('Введите новое число :')
        try:
            if new_element != 'stop':
                new_element = int(new_element)
                spisok.append(new_element)
            else:
                print(spisok)
                break
        except ValueError:
                print('Введите число !')
        else:
                print(spisok)


