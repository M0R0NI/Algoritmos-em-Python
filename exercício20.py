"""
Elaborar um programa que leia uma lista A com dez elementos inteiros. Construir uma lista B em que cada elemento da 
lista B deve ser o valor negativo do elemento correspondente da lista A.

"""

lista_A = [3, 10, 11, 2, 5, 15, 23, 87, 34, 10]
print(f"Lista A = {lista_A}")

lista_B = []
lista_B = [((i * 0) - i) for i in lista_A]   
print(f"Lista_B = {lista_B}")

