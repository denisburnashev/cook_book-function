cook_book = {}

def create_dict_from_file(file_name):
  with open(file_name, encoding = 'utf8') as book:
    for dish in book:
      dish = book.readline().lower().strip()
      num = book.readline().strip()
      ingridient_list = []
      cook_book.setdefault(dish, ingridient_list)
      for ingridient in range(int(num)):
        ingridient = book.readline().lower().strip().split(' | ')
        ingridient = {'ingredient_name' : ingridient[0], 'quantity' : ingridient[1], 'measure' : ingridient[2]}
        ingridient_list.append(ingridient)

create_dict_from_file('recipes.txt')


person_count = 1

dishes_list = []

for dishes in cook_book.keys():
  dishes_list.append(dishes)


def get_shop_list_by_dishes(dishes_list, person_count):
  for dishes, ingridient in cook_book.items():
    for product in ingridient:
      quantity_dict = {'measure' : product['measure'], 'quantity' : product['quantity']}
      edit_product = {product['ingredient_name'] : quantity_dict}
      for quantity in edit_product.values():
        quantity['quantity'] = int(quantity['quantity']) * person_count
      print(edit_product)

get_shop_list_by_dishes(dishes_list, person_count)
