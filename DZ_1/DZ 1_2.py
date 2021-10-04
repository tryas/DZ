# Задание 2 студент Радеев Дмитрий dradeev@gmail.com
# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_second = int(input("Введите время в секундах: "))
time_in_hours = time_in_second // 3600
time_in_minutes = (time_in_second - time_in_hours * 3600) // 60
time_in_sec = time_in_second - time_in_hours * 3600 - time_in_minutes * 60

print(f"Время = {time_in_hours}:{time_in_minutes}:{time_in_sec}")