# Задание 3_3 студент Радеев Дмитрий dradeev@gmail.com
#
# Реализовать функцию my_func(), которая принимает
# три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.

def my_func(a1, a2, a3):
        sum = a1 + a2 + a3 - min(a1, a2, a3)
        return(sum)

sum = my_func(10, 20, 40)
print('Результат : ', sum)
