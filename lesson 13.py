#For While

# while True:              #нужно указать условие выхода
#     print('Hello')


# s = 'hello world'
# for l in s:
#     if l == ' ':
#         continue           #переходим к следующей итерации цикла если != ' '
#     print(f'"{l}"', end=' ')


for i in 'Hello world':
    if i == ' ':
        break                 #когда находим пробел, то віходим из цикла
    print(i, end=' ')
else:
    print('\nNo spaces')