from collections import Counter 
from collections import namedtuple
from collections import OrderedDict
from collections import deque

c = "Contagem de objetos hasháveis."
my_counter = Counter(c)
print(my_counter)
print(list(my_counter.elements()))

Point = namedtuple('Point', 'a,b,c')
pt = Point(7, 10, -10)
print(pt.a, pt.b, pt.c)

ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)

d = deque()
d.append(1)
d.append(2)
d.appendleft(7)
print(d)


