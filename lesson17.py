#изменяеме и неизменяемые обьекты
#когда мы работаем с неизмняемыми типами, то пересоздается обьект, в ином случае, нет
# x = 10
# print(x, id(x))   #возвращает идентификатор обьекта
# x = 20
# print(x, id(x))

# s = 'hello'
# print(s, id(s))
# s += ' word'
# print(s, id(s))

# l = [1, 2, 3]         #обьект не пересоздается
# print(l, id(l))
# l.append(2)
# print(l, id(l))

# x = 10
# y = 10
#
# print(x, id(x))    #обьекті могут иметь одинаковій идентификатор
# print(y, id(y))
#
# x = 10
# y = 15
#
# print(x, id(x))
# print(y, id(y))

# l1 = [1, 2, 3]
# #l2 = l1
# #l2 = l1.copy()
# l2 = l1[:]
#                 # идентификатор будет одинаков, потому что мі ссілаемся на один и тот же обьект
# print(l1, id(l1))
# print(l2, id(l2))


#del - удаляет ключи, атрибуті, срезы и переменные

# x = 10
# print(x)
# del x
# print(x)