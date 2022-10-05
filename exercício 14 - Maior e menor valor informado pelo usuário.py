"""
Elaborar um programa que leia valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser 
apresentados o maior e o menor valores informados pelo usuário.

"""

maior = 0 
menor = 0
valor = 0

while valor >= 0:
    valor = int(input("Digite um valor qualquer: "))
    
    if valor > -1:
        if valor > maior:
            maior = valor
    
    else:
        menor = valor
        print(f"\nO menor valor informado pelo usuário é: {menor}.")
        print(f"O maior valor informado pelo usuário é: {maior}.")




