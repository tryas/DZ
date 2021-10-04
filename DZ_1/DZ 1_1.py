# Задание 1 студент Радеев Дмитрий dradeev@gmail.com
# Поработайте с переменными, создайте несколько, выведите на экран.
# Запросите у пользователя некоторые числа и строки и сохраните в переменные,
# затем выведите на экран.

variable_number = int(input("Введите число"))
print("Введенное число = ",variable_number, type(variable_number))

variable_string = input("Как Вас зовут?")
print("Привет,",variable_string)

variable_bool=int(input("Вы человек? Если Да, введите 1, если нет - 0"))
if variable_bool == 1:
    print(variable_string, ",Вы человек")
else:
    if variable_bool == 0:
        print(variable_string, ",Вы не человек" )
    else:
        print(variable_string, ",Вы человек, так как невнимательны")
age = int(input("Сколько Вам лет?"))
age_day = age * 365
print ("Вам ",age_day,"дней")

