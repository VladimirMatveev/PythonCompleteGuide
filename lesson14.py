# Списки

# l = [1,2,3, 'hello', ['test', 10], 'world', True]  #в список мі можем добавить любіе типі а так-же вложить списки
# Впорядкована колекция данных
# l2 = list('Hello')     #позволяет создать список из любой итерируемой последовательности
# l3 = list(((1, 2, 3)))   #кортеж
#
# l4 = [i for i in 'hello'] #генератор списка
#
# l5 = [i for i in 'hello world' if i not in ['l', ' ', 'w', 'o']]
#
# print(l5)



# l6 = (list(range(1, 11)))
# print(l6)


for i in range(1, 3):
    print(f'внешний цикл {i}')
    for j in range(1,3):
        print(f'внутренний цикл {j}')