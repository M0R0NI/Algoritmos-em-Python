"""
Elaborar um programa que leia valores positivos inteiros até que um valor negativo seja informado. Ao final devem ser 
apresentados o maior e o menor valores informados pelo usuário.

"""

valor = 0
q = 0
while valor >= 0:
    valor = int(input("Digite um valor qualquer: "))
    print(valor)
    
    q = 1 + q

    if valor <= -1:
        print(f"\nO menor valor informado pelo usuário é: {valor}")
        print(q)





