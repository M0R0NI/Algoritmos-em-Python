"""
Elaborar um programa que leia uma lista A com 15 elementos inteiros. Construir uma lista B, porém os elementos da lista B 
devem ser o quadrado dos elementos da lista A correspodente.

"""
lista_A = [3, 8, 1, 9, 15, 23, 40, 2, 9, 7, 17, 27, 3, 3, 13]
print(f"\nLista A = {lista_A}")

lista_B = [i * i for i in lista_A]    # Usando List Comprehension
print(f"Lista B = {lista_B}")

# Ou, de maneira "normal":

lista_C = [9, 7, 5, 3 , 1, 17, 34, 13, 2, 9, 7, 67, 17, 77, 13]
print(f"Lista C = {lista_C}")

lista_D = []
for i in lista_C:
    lista_D.append(i * i)    
print(f"Lista D = {lista_D}\n")