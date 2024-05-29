def hundred (chislo):
    сhislo = 100 / chislo
    print('результат деления: ', chislo)

try:
    chislo = int(input('введите число: '))
    a = 100 / chislo
except ValueError:
    print('ошибка! введенные данные не соответствуют целому числовому значению')
except ZeroDivisionError:
    print('ошибка! деление на ноль!!!')

hundred (chislo)