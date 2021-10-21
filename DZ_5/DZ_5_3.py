# Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
new_file = open("test_5_3.txt", 'r')
summa_oklad = 0
kol_rabotnikov = 0
for line in new_file:
    stroka = line.split(' ')
    summa_oklad = summa_oklad + int(stroka[1])
    if int(stroka[1]) < 20000:
        print('ФИО сотрудника с зп меньше 20 000', stroka[0])
    kol_rabotnikov = kol_rabotnikov + 1
print('Средний доход = ', summa_oklad / kol_rabotnikov )
new_file.close()

