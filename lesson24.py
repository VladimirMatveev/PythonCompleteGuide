#методы словаря

product1 = {'title': 'Sony', 'price': 100}
#print(product1.items())   #возвращает представление словаря - ключ\значение

# print(product1.items()) #возврат парі ключ и значение
# print(product1.keys())  # ключи
# print(product1.pop('title', 'NO'))      #удаляет ключ и возвращает значение
print(product1.popitem())             #удаляет и возвращает пару, если словар пуст то исключение ключошибка
# print(product1)
# print(product1.setdefault('title2', 'test'))  #возвращает значение елюча, если его нет, то создает елюч со значением дефолт
# product1.update({'test': 'value'})    #обносляет словар добавляя пары
# print(product1)
# print(product1.values())         #возвращает значение словаря

