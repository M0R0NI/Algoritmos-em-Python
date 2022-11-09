
import random

def jogada():
    user = input("Você escolhe pedra, papel ou tesoura?\n")
    computer = random.choice(["pedra", "papel", "tesoura"])

    def vitoria(jogador, oponente):
        if (jogador == "pedra" and oponente == "tesoura" or jogador == "tesoura" and oponente == "papel" \
            or jogador == "papel" and oponente == "pedra"):
            return True

    if user == computer:
        return "Houve um empate"

    if vitoria(user, computer):
        return "Você ganhou!"
    
    if not vitoria(user, computer):
        return "Você perdeu!"

print(jogada())
