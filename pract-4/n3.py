def magic (date):
    day = int(date / 1000000)
    month = int(date / 10000 % 100)
    year = int(date % 100)
    print('day: ', day, 'month: ', month, 'year: ', year)
    if day*month == year:
        print('Дата является магической!')
    else:
        print('Это обычная дата.')

date = int(input('введите дату в формате хх.хх.хххх, но без точек между числами: '))
magic(date)