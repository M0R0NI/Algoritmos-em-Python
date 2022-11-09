"""
Escrever um programa que apresente os valores da sequência numérica de Fibonacci até o décimo quinto termo. 
A sequência é formada pelos valores numéricos 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,... etc., 
obtendo-se o próximo termo a partir da soma do termo atual com o anterior sucessivamente até o infinito se a 
sequência não for interrompida. 
"""

from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

def Fibonacci(startNumber, endNumber):
    n = 0
    cur = F(n)
    while cur <= endNumber:
        if startNumber <= cur:
            print(cur)
        n += 1
        cur = F(n)
Fibonacci(1,1000)

from itertools import accumulate

f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
acc = accumulate(f)
print(list(acc))


