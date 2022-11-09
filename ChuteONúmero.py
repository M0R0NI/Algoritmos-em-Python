# Criar um algoritmo que gera um valor aleatório e o usuário tenha que acertar.

import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0 
        self.valor_minimo = 1
        self.valor_maximo = 777
        self.tentar_novamente = True
        self.q = 2

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()

        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print("Chute um valor mais baixo!")
                self.PedirValorAleatorio()

            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print("Chute um valor mais alto!")
                self.PedirValorAleatorio()
            if int(self.valor_do_chute) == self.valor_aleatorio:
                print("\nParabéns, você acertou!")
                print(f"Você acertou com apenas {self.q} tentativas.\n")
                self.tentar_novamente = False
        
            self.q = 1 + self.q

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

    
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()
