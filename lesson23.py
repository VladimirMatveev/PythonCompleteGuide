#словари
#
# produc1 = {'title': 'Sony', 'price': 100}
# produc2 = dict(title='Iphone', price=110)
#
# print(produc1)
# print(produc2)



# users = [
#     ['bob@gmail.com', "Bob"],
#     ['katy@gmail.com', "Katy"],
#     ['jonh@gmail.com', "Jonh"],
# ]
# d_users = dict(users)
# print(users)
# print(d_users)




# users = (                            #исходній кортеж
#     ('bob@gmail.com', "Bob"),
#     ('katy@gmail.com', "Katy"),
#     ('jonh@gmail.com', "Jonh")
# )
# d_users = dict(users)                #создаем словарь
# print(users)
# print(d_users)



# product = dict.fromkeys(['price1', 'price2', 'price3'])
# print(product)

# nums = {i: i + 1 for i in range(1, 10)}
# print(nums)



produc1 = {'title': 'Sony', 'price': 100}
produc2 = dict(title='Iphone', price=110)
#
# #print(produc2['price'])
# print(produc1.get('title2', "no"))   #if no key
#
#
# for key in produc1:
#     print(f'{key}: {produc1[key]}')


for key, value in produc1.items():
    print(key, value)


#список словарей
#
# products = [
#     {'title': 'sony', 'price': 100},
#     {'title': 'Iphone', 'price': 100},
#     {'title': 'Samsung', 'price': 100}
# ]
# print(products)
# for products in products:
#     print(products['title'], products['price'])