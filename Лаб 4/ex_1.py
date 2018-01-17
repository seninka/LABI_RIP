from librip.gens import field, gen_random


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стеллаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]
getr = gen_random(1, 5, 7)
print(*list(getr), sep=' ')

getf = field(goods, 'title')
print(*list(getf), sep=', ')
