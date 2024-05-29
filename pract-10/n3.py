with open('en-ru.txt', 'r', encoding='utf-8') as file:
    words = file.readlines()
dictionary = {}
for i in words:
    if '-' in i:
        eng, ru = i.strip().split('-')
        dictionary[ru]=eng
list_keys = list(dictionary.keys())
list_keys.sort()
with open('ru-en.txt', 'a+', encoding='utf-8') as file:
    for i in list_keys:
        file.write(f'{i} - {dictionary[i]}\n')




