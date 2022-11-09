from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import accumulate
import operator
from itertools import groupby
from itertools import count, cycle, repeat

import logging
logging.basicConfig(level=logging.INFO, filename="program2.log", format="%(levelname)s - %(asctime)s -  %(message)s")

a = [1, 2]
b = [3, 4] 
prod = product(a, b)
logging.info(list(prod))

a = [1, 2, 3, 4]
perm = permutations(a)
print(list(perm))
perm2 = permutations(a, 2)
logging.info(list(perm2))

a = [1, 2, 3]
comb = combinations(a, 2)
print(list(comb))  
comb_wr = combinations_with_replacement(a, 3)
print(list(comb_wr))   


a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))
#operator
acc2 = accumulate(a, func=operator.mul)
print(list(acc2))

def menor_que_3(x):
    return x < 3
a = [1, 2, 3, 4]
groupObj = groupby(a, key=menor_que_3)
for key, value in groupObj:
    print(key, list(value))
#exemplo 2:
persons = [{'name':"Carol", 'age': 23 }, {'name':"Julia", 'age': 23 }, {'name':"Bruna", 'age': 23 }, {'name':"Fernanda", 'age': 33 }, 
{'name':"Clara", 'age': 33 }, {'name':"Pamela", 'age': 22 }, {'name':"Vitoria", 'age': 28 }, {'name':"Lorena", 'age': 33},]
groupObj = groupby(persons, key=lambda x: x['age'])
for key, value in groupObj:
    print(key, list(value))

for i in count(10):
    if i == 17:
        break

"""
# cycle
a = [1, 2, 3]
for i in cycle(a): 
    print(i)

a2 = [1, 2, 3]
for i in repeat(1):
    print(i)
    
"""