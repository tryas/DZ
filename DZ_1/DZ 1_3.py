# Задание 3 студент Радеев Дмитрий dradeev@gmail.com
#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

input_numbers=input("Введите число: ")
summa = int(input_numbers) + int(input_numbers + input_numbers) + int(input_numbers + input_numbers + input_numbers)
print(summa)

