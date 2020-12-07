#6
a = int(input('a = '))
b = int(input('b = '))
day_number = 1
print(f'{day_number}-й день: {a} км')
while a <= b:
    a = a + 0.1 * a
    day_number = day_number + 1
    print(f'{day_number}-й день: {a} км')
print(f'Спортсмен достигнет результата на {day_number} день')