def happy(number):
    def summa(num):
        sum = 0
        for i in num:
            sum += int(i)
        return sum

    if len(number) % 2 == 0:
        halfIndex = int(len(number) / 2)
        firstHalf = number[0:halfIndex]
        secondHalf = number[halfIndex:len(number)]
        if summa(firstHalf) == summa(secondHalf):
            print('Счастливый билет!')
        else:
            print('Обычный билет')


number = str(input('введите ваш номер: '))
happy(number)