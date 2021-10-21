# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому
# предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
new_file = open('test_5_6.txt')
resultat = {}
file_lines = new_file.readlines()
for line in new_file:
    stroki_razdel = line.split()
    hours_predmet = '0'
    for el in lines[1:]:
        if el != ' ':
            hours_predmet = '0'
            for index in el:
                if index.isdigit():
                    hours_predmet = hours_predmet + index
                else:
                    break
            hours_predmet = hours_predmet + int(hours_predmet)
            print(hours_predmet)
    resultat.update({stroki_razdel[0].strip(':'): hours_predmet})
print(resultat)

