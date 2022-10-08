"""
Desenvolver um programa que leia cinco valores numéricos inteiros e no final apresente o total da soma de todos os 
elementos da matriz que sejam ímpares.

"""

q = 1
soma = 0

while q <= 5:
    valor = int(input("Digite um valor numérico inteiro: "))
    if valor%2 == 1:
        soma = soma + valor
        if q == 5:
            print(f"A soma de todos os números ímpares é: {soma}.")

    q = q + 1 

