# форматирование строк
name = 'John'
age = 60

#print('my name is ' + name + ', i`m' + age) #мы не можем сложить строку с другим типом
#print('my name is %(name)s i`m %(age)d' %{'name': name, 'age': age}) #именные маркеры
#print('my name is %s. i\'m %d' %(name, age)) #позиционные маркеры
#print('Title: %s, Price: %.2f' %('Sony', 40))

#FORMAT

# print('my name is {}. i`m {}'.format(name, age))
#print('my name is {0}. i`m {1}'.format(name, age)) #можно поставить номер позиции
#print('my name is {name}. i`m {age}'.format(name='andrey', age=age)) #именные аргументы

#Ctrl+alt+L переформатирование кода

#f-strings
#print(f'my name is {name}. i`m {age + 5}') #аргументы становятся как переменнные и можно производить операции
print(f'5 + 2 = {5 + 2}')
