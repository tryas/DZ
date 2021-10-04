# Задание 4 студент Радеев Дмитрий dradeev@gmail.com
# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

chislo = int(input("Введите целое положительное число"))
ostatok_max = 0
while chislo > 0:
    ostatok = chislo % 10
    chislo = chislo // 10
    if ostatok_max < ostatok:
        ostatok_max = ostatok
print(ostatok_max)
