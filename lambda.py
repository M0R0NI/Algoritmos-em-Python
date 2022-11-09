from functools import reduce

add10 = lambda x: x + 10 
print(add10(5))

def add10_func(x):
    return x + 10

mult = lambda x,y: x*y
print(mult(2, 7))

a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2,a)
print(list(b))
c = [x*2 for x in a]
print(c)
d = filter(lambda x: x%2==0, a)
print(list(d))

product_a = reduce(lambda x, y: x*y, a) # fatorial
print(product_a) 