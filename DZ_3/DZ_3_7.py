# Задание 3_7 студент Радеев Дмитрий dradeev@gmail.com

# Продолжить работу над заданием. В программу должна попадать строка
# из слов, разделённых пробелом. Каждое слово состоит из латинских букв
# в нижнем регистре. Нужно сделать вывод исходной строки, но каждое слово
# должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().

def int_func(new_string):
    new_string = new_string.title()
    return(new_string)

new_string = input('Введите строку слов из латинских букв в нижнем регистре :')
print('Обработанная строка: ', int_func(new_string))

