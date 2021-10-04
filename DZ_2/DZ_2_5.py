# Задание 2_5  студент Радеев Дмитрий dradeev@gmail.com
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_rating = [15, 11, 9, 9, 5, 3, 2]
new_element = int(input('Введите новый элемент рейтинга : '))
if new_element in my_rating:
    position = my_rating.index(new_element)
    my_rating.insert((position + 1), new_element)
else:
    my_rating.append(new_element)
my_rating.sort()
my_rating.reverse()
print(my_rating)

