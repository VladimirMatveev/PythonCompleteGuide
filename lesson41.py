#полиморфизм, возможность изменять функционал, унаследованный от базового класса
#перезружать методі и дополнять своим функционалом или переписывать как нужно
from classes import Person, Employee

person = Person('Katy', 9)
person.age = 39
person.print_info()
print(person)


employee = Employee('Nick', 30, 'Google')
employee.print_info()
employee.more_info()
print(employee)