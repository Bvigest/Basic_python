# 3
n = input('Введите n: ')
if int(n) > 0:
    digit = int(n) + int(n + n) + int(n + n + n)
    print(f'{n} + {n + n} + {n + n + n} = {digit}')
else:
    print('Введите положительное число')