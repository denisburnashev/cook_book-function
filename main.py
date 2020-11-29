cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ],
  }

person_count = 2

dishes_list = []

for dishes in cook_book.keys():
  dishes_list.append(dishes)


def get_shop_list_by_dishes(dishes_list, person_count):
  for dishes, ingridient in cook_book.items():
    for product in ingridient:
      edit_product = {}
      edit_product.setdefault(product['ingredient_name'], product)
      for quantity in edit_product.values():
        quantity['quantity'] = quantity['quantity'] * person_count
      del product['ingredient_name']
      print(edit_product)

get_shop_list_by_dishes(dishes_list, person_count)
