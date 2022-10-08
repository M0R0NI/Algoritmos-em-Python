"""
Elaborar um programa que leia 10 elementos para uma lista. Todo elemento que possui índice par deve ter seu elemento
dividido por 2. Caso contrário, os elementos devem ser multiplicados por 1.5.

"""

valores = list(map(int, input('Digite todos os valores: ').split()))
if int(valores <= 5):
    print(valores)

