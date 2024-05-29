import csv
with open('text.csv', 'r', newline='') as file:
    tabel = csv.reader(file)
    summa = 0
    next(tabel) #указатель+1
    for row in tabel:
        splitted_row = str(row[0]).split(';')
        product = splitted_row[0]
        kol = int(splitted_row[1])
        price = int(splitted_row[2])
        summa += kol * price
        print(product, ' - ', kol, ' шт. за ', price, ' руб.')
    print('Итоговая сумма: ', summa)

