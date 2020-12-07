vyruchka = int(input('Введите значение выручки: '))
izderzhka = int(input('Введите значение издержки: '))
if vyruchka > izderzhka:
    print('Поздравляем, вы успешный бизнесмен')
    renta = (vyruchka - izderzhka) / vyruchka
    print(f'Ваша рентабельность: {renta}')
    people_count = int(input('Введите кол-во сотрудников: '))
    print('Прибыль на 1 сотрудника равна: ', (vyruchka - izderzhka) / people_count)
elif vyruchka < izderzhka:
    print('Поздравляем, у вас убыточный бизнес')
else:
    print('Вы работаете в 0!')
