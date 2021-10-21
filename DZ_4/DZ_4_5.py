# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


first_list = [el for el in range(100,1001) if el % 2 == 0]
summa_first_list = reduce(lambda x,y: x*y, first_list)
print(first_list)
print(summa_first_list)
