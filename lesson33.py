f = open('file.txt', 'r', encoding='utf-8') #r указіваем режим явно
text = f.read(8)
text2 = f.read(8)
f.write('новая строка\n')   #можно прочесть некоторое количество символом, но можно прочитать и целиком
print(text, text2)
f.close()

# f = open('file.txt', 'a', encoding='utf-8')   #a для дозаписи
# f.write('новая строка\n')
# f.close()

# lines = ['Новая строка 1', 'Новая строка 2']
# f = open('file.txt', 'a', encoding='utf-8')
# for i in lines:
#     f.write(i + '\n')

#f.writelines(lines)
# f.writelines(f'{i}\n' for i in lines)
# f.close()

# f = open('file.txt', 'r', encoding='utf-8')
# for line in f:
#     print(line, end=' ')
# f.close()

lines = ['строка 1', 'строка 2']
f = open('file.txt', 'w', encoding='utf-8')  #если єтого файла нет, то создаст и запишет строку
f.writelines(f'{i}\n' for i in lines)
f.close()
