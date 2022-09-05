class Person:
    name = 'Bob'

    def __init__(self, name):
        self.name = name                 #конструктор класса, для инициализации атрибутов класса

    def print_info(self):
        print(f'Hello, my name is {self.name}')

