#  Создать текстовый файл (не программно), сохранить в нем несколько строк,
#  выполнить подсчет количества строк, количества слов в каждой строке.

new_file = open("test_5_2.txt", 'r')

# new_string = new_file.readlines()
# print(new_string)
# print('Количество строк : ', len(new_string))
stroka = 0
for line in new_file:
#    print('Количество букв в строке', stroka + 1, " :", len(line)-1)
    print('Количество слов в строке', stroka + 1, " :", line.count(' ') + 1)
    stroka = stroka + 1
print('Количество строк : ', stroka)
new_file.close()
