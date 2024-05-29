import json
with open('file.json', 'r', encoding='UTF-8') as file:
    products = json.load(file)
for i in products['products']:
    print(f'Название: {i['name']}')
    print(f'Цена : {i['price']}')
    print(f'Вес : {i['weight']}')
    if i['available'] == True:
        print('В наличии')
    else:
        print('Нет в наличии!')