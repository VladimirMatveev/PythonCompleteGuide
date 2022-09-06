#ОСНОВІ ооп КЛАССЫ и обьекты
class A:
    property1 = 'property 1'
    property2 = 'property 2'       #свойства класса
    name = 'guest'
    def say_hi(self, name=''):             #ключевое слово которое содержит в себе указатель на єкземпляр класса
        if name:
            return 'hi, ' + name
        else:
            return 'hello, ' + self.name


a = A()
b = A()

# a.property1 = 'property 1'
# a.property2 = 'property 2'
print(a.property1)
print(b.say_hi('John'))
