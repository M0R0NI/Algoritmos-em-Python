"""
Desenvolver um programa em que o usuário determine a quantidade de valores numéricos inteiros a serem fornecidos para uma 
pesquisa. No final, apresentar o total da soma de todos os elementos que sejam pares. 

"""

q = 1
par = 0
soma = 0

usuario = int(input("Quantos valores você deseja que sejam calculados? "))
while q <= usuario:
    valor = int(input("\nDigite um valor: "))
    if valor%2 ==0:
        soma = valor + soma
        if q == usuario:
            print(f"\nA soma de todos os valores pares é: {soma}\n")

    q = q + 1 

        