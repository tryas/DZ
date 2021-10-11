import random
my_list = ['Dima', 'Radeev']
#new_list = [el + 10 for el in my_list]
# с условиями
new_list = [el * 2  for el  in my_list if el != 'Radeev']
print(my_list)
print(new_list)

# С вложенными циклами
str_1 = 'Dima'
str_2 = 'Radeev'
str_3 = 'tryas'
new_str = [el1 + el2 + el3  for el1 in str_1 for el2 in str_2 for el3 in str_3]
print(new_str)

my_tuple = [2, 4, 6]
new_obj = [el + 10 for el in my_tuple]
print(new_obj)

new_my_list = [el * random.randint(0,5) for el in my_tuple]
print(new_my_list)
