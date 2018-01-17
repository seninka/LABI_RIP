# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        self.ignore_case = False if (kwargs.get('ignore_case') == None) else kwargs.get('ignore_case')
        self.seen = []
        self.items = iter(items)

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            val = self.items.__next__()
            val_cmp = val if self.ignore_case == False else str(val).lower()
            if val_cmp not in self.seen:
                self.seen.append(val_cmp)
                return val

    def __iter__(self):
        return self
