"""
Elaborar um programa que leia 15 valores numéricos e no final apresente o somatório da fatorial de cada valor lido.

"""
q = 1
fatorial = 1
soma = 0

while q <= 15:
    v1 = int(input("Digite o primeiro valor: "))

    for i in range (1, v1 + 1):
        fatorial1 = i * fatorial
        soma = fatorial1 + soma
        
    q = q + 1
    if q > 15:
        print("\nO somatório da fatorial de cada valor é = {}.".format(soma))
    
