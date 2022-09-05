from classes import Person
                            #инкапсуляция, сокрытие неких свойств
                             # _age, если есть такая переменная, то на уровне соглашения она считается защищенной
                             # для создания приватного свойства __age
person1 = Person('Katy')
person1.print_info()

person2 = Person('Bob')
#print(person2.__age)        #AttributeError: 'Person' object has no attribute '__age'
#print(person2._Person__age)    #полной инкапсуляции нет, и можно обратьтся таким способом к нашему свойству
# print(person2.get_age())
# person2.set_age(100)
print(person2.age)
person2.age = 35
person2.print_info()
