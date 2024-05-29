words = []
while True:
    print('Напишите слово или "stop" чтобы остановиться')
    resp = input()
    if resp == 'stop':
        break
    words.append(resp)
print(' '.join(words))