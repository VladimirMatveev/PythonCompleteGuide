class Person:

    def __init__(self, name):
        self.name = name
        self.__age = 20

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
