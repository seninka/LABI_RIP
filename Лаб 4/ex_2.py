from librip.gens import field, gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1,3,10)

print(list(Unique(data1)))
print(list(Unique(data2)))
print(list(Unique(['a', 'A', 'b', 'B'])))
print(list(Unique(['a', 'A', 'b', 'B'], ignore_case = True)))
