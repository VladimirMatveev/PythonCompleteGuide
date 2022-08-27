# множества, неупорядоченная коллекция/ не поддерж индексиров

# s = {'apple', 'orange', 'apple', 'pear', 'banana', 'orange'}
# s2 = set('hello') #создать множество
# s3 = {i for i in range(1, 11)}
# s4 = {5, 3, 11, 2}       #???
# s5 = {}    #пустіе скобки будет тип словарь
#
#
# print(s)
# print(s2)
# print(s3)
# print(s4)
#
# nums = [1, 2, 3, 4, 5, 6]
# nums2 = set(nums)
# print(nums2)


#операции над ними

# a = set('abracadabra')
# b = set('alacazam')
# c = a - b       #Вычитание, убираем из а все буквы, шо есть в б
# d = a | b       #обьединение - буквы или в а или в б
# e = a & b       #пересечение - буквы и в а и в б
# f = a ^ b       #множество из элементов = буквы в а или б, но не в обоих
#
# print(a, b, c, d, e, f, sep='\n')

#методы

s = {'apple', 'orange', 'apple', 'pear', 'banana', 'orange'}
# s2 = s.copy()
#
# print(s, id(s))
# print(s2, id(s2))

# s.add('melon')
# print(s)

# s.discard('apple') #удаляет єлемент
# print(s)


# заморож множество, нельзя изменить
a = frozenset('hello')
print(a)


for i in s:
    print(i)

