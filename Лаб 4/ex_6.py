import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = None

path = sys.argv[1]
print(path)

with open(path) as f:
    data = json.load(f)

@print_result
def f1(data):
    return sorted(list(unique(list(field(data, 'job-name')), ignore_case=True)))

@print_result
def f2(data):
    return list(filter(lambda x: x[0, 11].lower() == 'программист', data))

@print_result
def f3(data):
    return list(map(lambda x: x+' с опытом Python', data))

@print_result
def f4(data):
    return (list('{} с зарплатой {} раблей'.format(prof, salary) for prof, salary in zip(data, gen_random(100000, 200000, len(data)))))

with timer():
    f4(f3(f2(f1(data))))
