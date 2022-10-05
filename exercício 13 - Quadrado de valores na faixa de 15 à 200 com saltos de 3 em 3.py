"""
Elaborar um programa que apresente os quadrados dos valores inteiros existentes na faixa de valores de 15 a 200 com saltos 
de 3 em 3. 

"""

for i in range(15, 200, 3):
    quadrado = pow(i, 2)
    print(quadrado)