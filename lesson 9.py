# s = r'C:\d\new.txt' # \\, r-обьявляем сырок строкой, не обрабатывает управляющие последовательности
# print(s)

# s = 'py' 'thon' #склеивание строк
# print(s)

# s1 = 'hello'
# s2 = 'world'
# s3 = s1 + s2
# print(s3)

# name = 'John'
# age = 22
# print('my name is ' + name + ' im ' + str(age)) #использ функц

#print('hi ' * 5)

#индексация строк

#s = 'hello world'
# print(s[2], s[4], s[0])
#print(s[12]) #ошибка

#s[0] = 'd' # ошибка, строки не изменяемі, мы можем создать лишь новую строку

s = 'hello world'
print(s[0:12]) #срез строки
print(s[-1])
print(s[6:]) #если не указать аргумент то мы получим длинну строки
print(s[::-1]) #3 аргумент єто шаг
print(s[:5] + s[6:]) #складываем строки
print(s[1])
