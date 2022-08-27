#комментирование функций  """ """. ctrl + q
# def get_sum(a, b):
#     """
#     возвращает сумму аргументов а и b
#
#     :param a: первый операнд
#     :type a: int
#     :param b: второй операнд
#     :type b: int
#     :return: Return type int
#     """
#     return a + b
#
# print(get_sum(1, 2))


#области видимости (локальная и глобальная), она определяет контекст пересенной
# вне функции глобальная область, внутри функции локальній контекст видимости и они доступны только внутри функции

# a = 5 #global
# #однако она доступна только на чтение внутри функции
# def f():
#     a = 10 #local
#     a += 1
#     print(a)
#
# print(a)
# f()
# print(a)


# a = 5
# def f():
#     global a       #можес с помощью функции брять глобальную переменную
#     a += 1
#     print(a)
#
# f()


# l = [1, '2', 3]
#
# def f(l):
#     return [i * 2 for i in l]
#
# print(f(l))
#
# def f2(l):
#     def get_mult(x):
#         return int(x) * 2                  #можно віполнять много действий, и возвращать результат одним вызовом
#     return [get_mult(i) for i in l]   #для каждого і мы вызываем функцию гетмалт, функция принимает х, и возвращает элемент *2
# print(f2(l))
#
#
# def f3(l):
#     def get_mult(x):
#         if isinstance(x, int):
#             return x * 2
#     return [get_mult(i) for i in l if get_mult(i)]
#
# print(f3(l))
#
#
#
#
# def f4(l):
#     def get_mult(x):
#         return x * 2
#     return list(map(get_mult, l))          #применяет к каждому жлементу последовательности функцию
#
# print(f4(l))

#####################################################################################
#вернуть тру или фолс, индекс эелемента одд ==(), найти индекст в списке
def add_ball(elem):
    return elem.index("odd") in elem

print(add_ball(["even",4,"even",7,"even",55,"even",6,"odd",8,"even"]))  #True
print(add_ball(["even",4,"even",7,"even",55,"even",6,"odd",3,"even"]))  #False
print(add_ball(["even",6,"odd",2,"even"]))  #True

#####################################################################################
'''
написать функцию find_sum(n), где аргумент функции єто конечній элемент последователности включительно
функция должрна вернуть сумму всех чисел кратных 3 или 5
'''


s = "the-stealth-warrior"
print(s.replace('-', ''))

