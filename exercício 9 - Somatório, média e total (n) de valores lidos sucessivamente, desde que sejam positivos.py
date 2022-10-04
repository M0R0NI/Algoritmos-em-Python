"""
Elaborar um programa que leia sucessivamente valores numéricos e apresente no final o somatório, a média e o total
dos valores lidos. O programa deve ler os valores enquanto o usuário estiver fornecendo valores positivos. Ou seja, 
o programa deve parar quando o usuário fornecer um valor negativo.

"""

valor = 0
soma = 0 
q = 1

while valor >= 0:
    valor = int(input(f"\nDigite um valor qualquer: "))
    soma = valor + soma
    media = soma / q 

    print(f"\nO somatório dos valores é = {soma}.")
    print(f"A média dos valores é = {media}.")
    print(f"O total de valores lidos é = {q}.\n")
    
    q = q + 1