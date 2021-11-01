# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать
# их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
class Data:
    day = '01'
    month = '01'
    year = '1900'

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def izvl_day(cls, date_str): # извлечение из date_str числа, месяца, года 24-03-1967
        return (int(date_str[0:2]))

    @classmethod
    def izvl_month(cls, date_str):
        return (int(date_str[3:5]))

    @classmethod
    def izvl_year(cls, date_str):
        return (int(date_str[6:10]))


    @staticmethod
    def proverka(date_str):
        day = int(date_str[0:2])
        month = int(date_str[3:5])
        year = int(date_str[6:10])
        if (day < 31 and day > 0) and (month < 12 and month > 0) and (year > 0):
            return day, month, year
        else:
            print('Введите правильную дату')


# my_date = Data('24-03-1967')
# print(my_date)
my_date = '24-15-1967'
Data.proverka(my_date)
print(Data.izvl_day(my_date))
print(Data.izvl_month(my_date))
print(Data.izvl_year(my_date))
