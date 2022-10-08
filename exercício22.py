"""
Escrever um programa que leia 10 elementos para temperaturas em graus Celcius em uma Lista. Construir uma lista 
Fahrenheit em que cada elementos da deve ser a conversão em temperatura em graus Fahrenheit do elemento correspodente da 
Lista Celcius.

"""
lista_celcius = [30, 19, 25, 39, 23, 10, 9, 13, 27, 29]
print(f"Temperatura em Graus Celcius: {lista_celcius}")

lista_fahrenheit = []
for i in lista_celcius:
    lista_fahrenheit.append((i * 9/5) + 32)
print(f"Temperatura em Graus Fahrenheit: {lista_fahrenheit}")
