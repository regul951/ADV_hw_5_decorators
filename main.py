# 1. Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
# имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
#
# 2. Написать декоратор из п.1, но с параметром – путь к логам.
#
# 3. Применить написанный логгер к приложению из любого предыдущего д/з.

import datetime


def log_path(path):
    def decor_func(old_func):
        def new_func(*args, **kwargs):
            arguments = f'{args}, {kwargs}'
            start = datetime.datetime.now()
            result = old_func(*args, **kwargs)
            file_path = path
            with open(file_path, 'w', encoding='utf-8') as f:
                data = f'Имя функции: {old_func.__name__}\n'\
                       f'Дата и время вызова функции: {start}\n'\
                       f'Аргументы функции: {arguments}\n'\
                       f'Результат: {result}'
                f.write(data)
            return result
        return new_func
    return decor_func

# ___Список блюд___
with open("recipes.txt", "r", encoding='utf-8-sig') as f:
    cook_book = {}

    while True:
        name = f.readline().rstrip()
        if not name:
            break
        number = int(f.readline().rstrip())
        ingredient = []
        for i in range(number):
            split_str = f.readline().rstrip().split(' | ')
            ingredient_list = {'ingredient_name': split_str[0],
                               'quantity': int(split_str[1]),
                               'measure': split_str[2]}
            ingredient.append(ingredient_list)
        f.readline()
        cook_book[name] = ingredient
# _____________

@log_path('function_result.txt')
def get_shop_list_by_dishes(dishes=[], person_count=0):
    list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book:
            cook_book_dish = cook_book[dish]
            for i in cook_book_dish:
                quantity_i = 0
                if i['ingredient_name'] in list_by_dishes:
                    quantity_i = list_by_dishes[i['ingredient_name']]['quantity']
                list_by_dishes.update(
                    {i['ingredient_name']: {'measure': i['measure'],
                                            'quantity': quantity_i + i['quantity'] * person_count}
                     })
        else:
            return f'Блюдо \'{dish}\' отсутствует, проверьте правильность ввода.'
    return list_by_dishes

get_shop_list_by_dishes(['Маца'], 1)
