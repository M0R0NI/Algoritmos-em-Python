# conjuntos
# Conjunto tem por caracteristica não duplicar elementos.

myset = {1, 2, 3, 4, 5, 5, 5, 8, 6, 7, 7}
print(myset)

myset = set("Hello")
print(myset)

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.add(4)
myset.remove(3)
print(myset)

setA = {10, 20, 25, 35, 70, 50, 60, 77, 100}
setB = {11, 30, 35, 77, 20, 25, 10, 12, 100}
dif = setA.difference(setB)
print(dif)
dif2 = setB.difference(setA)
print(dif2)
dif3 = setA.symmetric_difference(setB)
print(dif3)
setA.update(setB)
print(setA)
setA.intersection_update(setB)
print(setA)
