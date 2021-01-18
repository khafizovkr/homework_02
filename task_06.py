item_number = 0
item_dict = {'название': None, 'цена': None, 'количество': None, 'ед': None}

item_list = []
while True:
    item_number += 1
    item_tuple = []
    item_dict['название'] = input('Введите название товара: ')
    item_dict['цена'] = int(input('Введите цену товара: '))
    item_dict['количество'] = int(input('Введите количество товара: '))
    item_dict['ед'] = input('Введите единицу измерения: ')
    item_tuple.append(item_number)
    item_tuple.append(item_dict.copy())
    item_tuple = tuple(item_tuple)
    item_list.append(item_tuple)
    print(item_list)
    continue_check = input("Продолжаем: ")
    if continue_check == 'No' or continue_check == 'Нет':
        print(f'Список товаров: {item_list}')
        break

item_name = []
item_price = []
item_amount = []
item_unit = []
for item in item_list:
    for el in item[1:]:
        item_name.append(el['название'])
        item_price.append(el['цена'])
        item_amount.append(el['количество'])
        item_unit.append(el['ед'])
key_list = ['название', 'цена', 'количество', 'ед']
value_list = [item_name, item_price, item_amount, item_unit]
analytics = dict(zip(key_list, value_list))
print(analytics)