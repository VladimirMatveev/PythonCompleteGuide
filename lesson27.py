# def set_register(s):
#     if ' ' in s:
#         return s.upper()
#     else:
#         return s.lower()
#
# print(set_register('Hello World'))
# print(set_register('Hello,World'))

# def get_sum(a, b, c=0, d=1):        #позиционных и именованных аргумента
#     return a + b + c + d

#print(get_sum(1, 2, 3, 4))    #позационные аргументы, при взове, каждый из них соответствует позиции описания функции
#print(sep='', 'hello')        #именнованніе аргументы должны идти до ключевого аргумента
# print(get_sum(1, 2, d=5))


#произвольное количество аргументов
# def get_num(*args):          #(*args, **kwargs): кортеж и словарь, позиционніе аргументі и именованніе аргументі, ключ словарь и условное название
#     print(args)
#     return sum(args)
#
# print(get_num(1, 5, 10))

def funk(**kwargs):
    print(kwargs)    #стало словарем
funk(a=1, b=5, c=20)



def f(a, x, *args, **kwargs):      #args/kwargs опциональні, они могуть біть или не біть
    print(a)
    print(x)
    print(args)
    print(kwargs)
                                  #позиционніе и именованніе можно комбинировать при  этом позиционные идут впереди
f(1, 2, 3, 4, b='test', c='hi')
f(1, 2)