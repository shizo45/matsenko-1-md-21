def division(chislo):
    if chislo % 3 == 0:
        print('Число кратно трем!')
    else:
        print('Число не делится на три!')
chislo = int(input('Введите число: '))
division(chislo)