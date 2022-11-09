"""
Crie um programa em que o usuário deve  acertar um número aleatório gerado pelo próprio programa. Depois, dê o número de 
tentativas do usuário.

"""
import random

def adivinhar(x):
    random_number = random.randint(1, x) # Função capaz de gerar números aleatórios. Parâmetros: (início, fim). Ambos devem ser valores aleatórios.
    adivinhar = 0 
    q = 0
    while adivinhar != random_number:
        adivinhar = int(input(f"Adivinhe um número entre 1 e {x}: "))
        if adivinhar < random_number:
            print("Você digitou um número menor. Tente novamente.")
        elif adivinhar > random_number:
            print("Você digitou um número maior. Tente novamente.")

        q = 1 + q 

    print(f"Parabéns, você acertou o número aleatório é {random_number}!")
    print(f"O número de tentativas foi de: {q}")

adivinhar(10)



          