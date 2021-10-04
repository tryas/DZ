# Задание 2_4 студент Радеев Дмитрий dradeev@gmail.com
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
new_string = input('Введите строку из нескольких слов, разделенных пробелами : ')
# numbers_word = new_string.count(' ') + 1
new_list = new_string.split(' ')
index = 1
for el in new_list:
    print(index, el[0:10])
    index = index + 1





# for el in new_list:
#     if len(el) <= 10:
#         print(index, el)
#     else:
#         print(index, el[0:10])
#     index = index + 1
# # print(new_string)
# # print(new_list)