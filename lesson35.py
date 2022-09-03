# try:
#     num = 100 / 0
# except ZeroDivisionError:
#     num = 0
# except TypeError:
#     num = 1
#print(num)
# try:
#     num = 100 / 0
# except Exception:
#     print(Exception)
#     num = 1
# else:
#     print('Else')      #выводится в случе если нету ошибок а файнали всегда
# finally:
#     print('Finally')
#
# print(num)

while True:
    try:
        num = int(input('enter your number: '))
        print(f'100 / {num} = {100/num}')
        break
    except ZeroDivisionError:
        print('The number must be greater than zero')
    except ValueError:
        print('Must be a number')
