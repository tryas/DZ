# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
import random

new_file = open('test_5_5.txt', 'w')
new_file = open('test_5_5.txt', 'a')
count = 0
summa = 0
while count < 100:
    new_numbers = random.randint(0, 100)
    new_file.write(f'{new_numbers} ')
    new_file.write(' ')
    summa = summa + new_numbers
    count = count + 1
print('Summa = ', summa)

new_file.close()
