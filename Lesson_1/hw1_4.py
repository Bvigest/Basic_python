# 4
in_digit = int(input('Введите число: '))
max_digit = 0
if in_digit < 10:
    print(in_digit)
else:
    while 0 < in_digit:
        digit = in_digit % 10
        if digit > max_digit:
            max_digit = digit
        in_digit = in_digit // 10
    print(f'Максимальная цифра в числе: {max_digit}')