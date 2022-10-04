"""
Elaborar um programa que apresente como resultado os quadrados armazenados na memória dos números inteiros 
existentes na faixa de valor de 15 a 20.

"""

for faixa in range (15, 201):
    quadrado = pow(faixa, 2)
    print(f"\nO quadrado de {faixa} é {quadrado}\n")
    