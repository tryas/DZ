# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
firmy = {}
kol_pribyl_firm = 0
summa_pribyl = 0
with open('test_5_7.txt') as file:
    lines = file.readlines()
    for el in lines:
        pokazateli = el.split()
        pribyl = int(pokazateli[2]) - int(pokazateli[3])
        firmy.update({pokazateli[0]: pribyl})
        if pribyl > 0:
            kol_pribyl_firm = kol_pribyl_firm + 1
            summa_pribyl = summa_pribyl + pribyl
sred_pribyl = summa_pribyl / kol_pribyl_firm
resultat = [firmy, {'srednya pribyl' : sred_pribyl}]
print(resultat)
with open('resultat.json', 'w') as file:
    json.dump(resultat, file)
