def read_recipes_from_file(filename):  # функция получает список из текстового файла с рецептами
    cook_book = {}
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            i += 1
            if not lines[i].strip().isdigit():
                i += 1
                continue
            ingredient_count = int(lines[i])
            ingredients = []
            for j in range(ingredient_count):
                ingredient_info = lines[i + 1 + j].strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_info[0],
                    'quantity': int(ingredient_info[1]),
                    'measure': ingredient_info[2]
                }
                ingredients.append(ingredient)
            cook_book[dish_name] = ingredients
            i += 1 + ingredient_count
    return cook_book


recipes_file = 'recipes.txt'
cook_book = read_recipes_from_file(recipes_file)


# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):  # функция принимает на вход список блюд и кол-во персон,
    # а на выходе получает словарь с названием ингредиентов и его количества для блюда
    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']
            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[ingredient_name]['quantity'] += quantity

    sorted_shop_list = {k: shop_list[k] for k in sorted(shop_list)}
    return sorted_shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
