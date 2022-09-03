#кортежи (неизменяемый)
# t1 = (1, 2, 3)
# t2 = 1, 2, 3        #упаковка кортежа
# t3 = tuple((1, 2, 3))    #конструктор тупле
# t1 = (1,)
# # t1 = tuple('hello')
# t1 = (1, 2, 3)

# print(t1.__sizeof__())

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3.count('l'))
#
#
# if 'a' in t3:
#     print(t3.index('l'))
# else:
#     print('no')
#
#
# for i in t3:
#     if i == ' ':
#         continue
#     print(f'"{i}"', end=' ')

#можем поместить в кортеж изменяемій список

# t1 = (11, 10, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t1, id(t1))
# t1[4][0] = 'new'
# t1[4].append('hello')
# print(t1, id(t1))

# распаковка кортежа

# t1 = (1, 2, 3,)
# x, y, z = t1
#
# print(x, y, z)


# x = 1
# y = 2
# print(x, y)
# x, y = y, x
# print(x, y)


# words = ['мадам', 'топот', 'test', 'madam', 'word']
# pol = []
# for words in words:                      #берем каждый элемент, переворачиваем и сравниваем с исходным вариантом
#     if words == words[::-1]:
#         pol.append(words)          #тогда мы в список добавляем полиндром
# print(pol)

# my_str = ['Око за око', 'А роза упала на лапу Азора', 'Около Миши молоко']
# pol1 = []
# for word in my_str:
#         res = word.replace(' ', '').lower()
#         if res == res[::-1]:
#             pol1.append(word)
# print(pol1)