import random


# Генератор вычленения полей из массива словарей
# Пример:
# goods = [
#    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            val = item.get(args[0])
            if val != None:
                yield val
        else:
            res = {};
            for item_arg in item:
                if (item_arg in args) and (item[item_arg] != None):
                    res[item_arg] = item[item_arg]
            if res != {}:
                yield res
    # Необходимо реализовать генератор

# Генератор списка случайных чисел
# Пример:
# gen_random(1, 3, 5) должен выдать примерно 2, 2, 3, 2, 1
# Hint: реализация занимает 2 строки
def gen_random(begin, end, num_count):
    for i in list(range(num_count)):
        yield random.randint(begin,end)

