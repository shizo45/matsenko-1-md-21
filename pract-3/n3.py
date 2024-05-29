words = []
while True:
    print('Напишите слово')
    resp = input()
    if resp == 'stop':
        break
    if "Ф" in resp or "ф" in resp:
        print('Ого! Это редкое слово!')
    else:
        print('Эх, это не очень редкое слово…')