# #функции
#
# def hello(name, word):               #param
#     print('hello, ' + name + '. Say ' + word)
#
# hello('John', 'beee')                     #для того, чтобы вызвать функцию, нам нужно к ней обратиться
# hello('Katty', 'hi')                    #если у нас строка, то аргумент мі передаем в ковічке, ессли нет, то так
# hello('Bob', 'hi')                    #место нашего name, мы указали то, что мы передали в качестве параметра функции


# def get_sum(a, b):    #лучше не назівать функцию встроенными функциями
#     print(a + b)

# a = 2                 #то что мы указываем в качестве аргументов, никак не связано с тем, как мы вызываем функцию
# b = 5                 #можно просто указать параметрі или определить переменніе, все будет работать
# get_sum(1, 3)
# get_sum(a, b)

# def get_sum(a, b):
#     return a + b
#                  #если функция возвращает результат, то нам нужно сохранить в перемен или сразу распечатать
# print(get_sum(1, 2))                #хорошим тоном является возвращать результат  return


# def hi():
#     print('hello')      #когда мы не используем ретерн то функция что-то неявно возвращает
#                         #если функция уже что-то печатает, то ее еще раз не нудно печатать
# print(hi())