# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.

import math

class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.img + other.img).to_str()

    def __mul__(self, other):
        first = self.real * other.real - self.img * other.img
        return ComplexNumber(first, self.real * other.img + other.img * self.real).to_str()

    def to_str(self):
        return str(self.real) + '+' + str(self.img) + 'j'


some_number = ComplexNumber(1, 2)
another_number = ComplexNumber(2, 4)
print(some_number.__mul__(another_number))
print(some_number.__add__(another_number))