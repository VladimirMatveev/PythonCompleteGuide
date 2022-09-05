class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.__age}')

    # def get_age(self):              #гет получает свойство сет устанавливает
    #     return self.__age           #получаем возраст
    #
    # def set_age(self, value):           #с помощью сеттера мі можем контролить установленное значение
    #     if value in range(1, 101):      #устанавливаем возраст
    #         self.__age = value
    #     else:
    #         print('Wrong age')
    @property               #декоратор, преврощается в метод геттер
    def age(self):
        return self.__age
                               #сеттер должен быть после геттера, иначе будет ошибка
    @age.setter            #декоратор сеттер
    def age(self, value):
        if value in range(1, 101):
            self.__age = value
        else:
            print('Wrong age')
    def __str__(self):
       #return f'Name: {self.name}'
        return 'Class ' + self.__class__.__name__


class Employee(Person):

    def __init__(self, name, age, company):
        super().__init__(name, age)      #обращаемся к методу инит родительского суперкласса и отдаем два параметра нейм и адж
        self.company = company

    def more_info(self):
        print(f'Name: {self.name} works in {self.company}')

    def print_info(self):
        super().print_info()
        print(f'Work: {self.company}')

    def __str__(self):
       #return f'Name: {self.name}'
        return 'Class ' + self.__class__.__name__