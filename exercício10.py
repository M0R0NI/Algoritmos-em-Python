"""
Elaborar um programa que leia dez valores numéricos reais e apresente no final o somatório e a média dos valores 
lidos.

"""
q = 1
soma = 0 

while q <= 10:
    v1 = float(input("Digite um número: "))
    soma = v1 + soma
    media = soma / q
    print(f"\nSomatório dos valores lidos = {soma}.")
    print(f"Média dos valores lidos = {media}.\n")

    q = q + 1 

