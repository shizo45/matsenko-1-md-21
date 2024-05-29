N = int(input ('Введите количество слов' ))
i=1
words = []
while i <= N:
    words.append(input())
    i += 1
print(' '.join(words))