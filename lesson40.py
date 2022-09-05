#наследование, позволяет создавать новый класс на основе уже существующего
from classes import Person, Employee

employee = Employee('Nick', 30)
employee.print_info()
employee.more_info()

# Для класса Имплои доступны через ключевое слово Self, все методы и атрибуты класса персон которые являются открытыми