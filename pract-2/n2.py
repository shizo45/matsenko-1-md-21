n = int (input('Введите номер места: '))
print ()
if n%2==0 and n < 37:
        print('верхнее купе')
elif n > 37 and n%2==0:
        print('верхнее боковое')
elif n < 37 and n%2!=0:
        print('нижнее купе')
else:
        print('нижнее боковое')