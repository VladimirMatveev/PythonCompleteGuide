#модули ядра

#from datetime import date, datetime, timedelta

#дата и время
#date

# today = date.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.weekday()) # c 0 до 6

#datetime
#now = datetime.now()
# now1 = datetime.today()
# print(now ,'\n', now1)
# print(now.day)
# print(now.month)
# print(now.year)
# print(now.weekday())
# print(now.hour)
# print(now.minute)
# print(now.second)


# days = ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс']
# print(days[now.weekday()])

# import locale
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
#
# print(now.strftime('%a')) #маркері, сокращение
# print(now.strftime('%A'))
#
# print(f'дата: {now.strftime("%A, %d %b %Y")}')
# print(f'дата: {now.strftime("%H: %M: %S")}')
#
# print(now.strftime("%c"))
# print(now.strftime("%x"))
# print(now.strftime("%X"))



#timedelta


# print(now.strftime("%c"))
# d1 = now + timedelta(days=1, hours=2, minutes=10)
# print(d1.strftime('%c'))


# import os
# os.mkdir('Folder')
# for i in range(2):
#     os.mkdir('C:/Users/mylit/PycharmProjects/pythonCompleteGuide1/')

import os

for root, dirs, files in os.walk('Folder'):
    level = root.count(os.sep)
    indent = ' ' * 4 * level
    print(f'{indent}[{os.path.basename(root)}]')
    sub_indent = ' ' * 4 * (level + 1)

    for file in files:
        print(f'{sub_indent}{file}')