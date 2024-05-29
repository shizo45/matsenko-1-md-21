import json
with open('file.json', 'r', encoding='UTF-8') as file:
    products = json.load(file)

new_product = {}
new_product['name'] = input('Введите название продукта: ')
new_product['price'] = int(input('Введите цену продукта: '))
new_product['available'] = bool(input('Введите наличие продукта: '))
new_product['weight'] = int(input('Введите вес продукта (г): '))
products['products'].append(new_product)

for i in products['products']:
    print(f'Название: {i['name']}')
    print(f'Цена : {i['price']}')
    print(f'Вес : {i['weight']}')
    if i['available'] == True:
        print('В наличии')
    else:
        print('Нет в наличии!')

