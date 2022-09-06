# i = 2
# n = 2
# while i < 11: #2
#     while n < 11: #2
#         print(n, '*', i, '=', n * i, end='\t')
#         n += 1
#     print('\t')
#     n = 2
#     i += 1

for i in range(2, 11):
    for n in range(2, 11):
        print(f'{n} * {i} = {n * i}\t', end='')
    print('')
