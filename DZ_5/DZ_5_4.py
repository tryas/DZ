# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

old_file = open('test_5_4', 'r')
new_file = open('test_5_4_new.txt', 'a')

perevod = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре',
           }

stroki = old_file.readlines()
for line in stroki:
    stroka = line.split(' ')
    chislo = perevod.get(stroka[0])
    new_file.write(line.replace(stroka[0], chislo))

old_file.close()
new_file.close()


