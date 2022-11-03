
def open_book():
    with open('file1.txt', 'r', encoding='utf-8') as recipes:
        cook_book = {}
        for line in recipes:
            dish_name = line.strip()
            ingredient_count = int(recipes.readline())
            ingredients = []
            for _ in range(ingredient_count):
                ingredient = recipes.readline().split(' | ')
                name, quant, meas = ingredient
                ingredients.append({'ingredient_name': name,
                                    'quantity': quant,
                                    'measure': meas.strip()})
            recipes.readline()
            cook_book[dish_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    cook = open_book()
    for dish in dishes:
        for name, ingredients in cook.items():
            if name == dish:
                for ingredient in ingredients:
                    if ingredient['ingredient_name'] in shopping_list.keys():
                        measure, quantity_now = shopping_list[ingredient['ingredient_name']].values()
                        quantity = int(ingredient['quantity']) * person_count + quantity_now
                        shopping_list[ingredient['ingredient_name']] = {'measure': measure,
                                                                        'quantity': quantity}
                    else:
                        quantity = int(ingredient['quantity'])*person_count
                        shopping_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                        'quantity': quantity}
    return shopping_list

print(open_book(),'\n')

print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
