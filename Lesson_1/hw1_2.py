# 2
in_sec = int(input('Время в секундах: '))
print(in_sec)
hour = in_sec // 3600
min = (in_sec % 3600) // 60
sec = in_sec  - hour * 3600 - min * 60
print(f'{hour:02}:{min:02}:{sec:02}')