# Задание 2_2 студент Радеев Дмитрий dradeev@gmail.com
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

new_list=[]
new_element = None
while new_element != '' :
    new_element = input('Введите элемент списка : ')
    if new_element != '':
        new_list.append(new_element)
        print(new_list)
    else:
        print('Итоговый список : ',new_list)

lenght_new_list = len(new_list)
i = 0
while i < (lenght_new_list -1):
    temp = new_list[i+1]
    new_list[i+1] = new_list[i]
    new_list[i] = temp
    i = i + 2
print(new_list)