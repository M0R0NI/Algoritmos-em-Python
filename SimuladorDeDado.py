# Gerando um valor de 1 à 6.

import random  # Importar biblioteca:
    
class SimuladorDeDado:

# Definição das configurações iniciais. Neste caso precisamos de um valor inicial e um valor final.
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Deseja jogar o dado? "
        self.mensagem1 = "Deseja jogar novamente o dado? "

    def Iniciar(self):
        resposta = input(self.mensagem)

        try:   # Se o correr algum tipo de excessão o programa apresentará a resposta em "Except".
            if resposta == "sim" or resposta == "s":
                self.GerarValorDoDado()
            elif resposta == "não" or resposta == "n":
                print("Programa encerrado!")
            else:
                print("Favor digitar 'sim' ou 'não'.")
        except:
            print("Ocorreu uma falha ao receber sua resposta.")

        if resposta == "sim" or resposta == "s":    
            resposta1 = input(self.mensagem1)
            try:   # Se o correr algum tipo de excessão o programa apresentará a resposta em "Except".
                if resposta1 == "sim" or resposta1 == "s":
                    self.GerarValorDoDado()
                elif resposta1 == "não" or resposta1 == "n":
                    print("Programa encerrado!")
                else:
                    print("Favor digitar 'sim' ou 'não'.")
            except:
                print("Ocorreu uma falha ao receber sua resposta.")

            while resposta1 == "sim" or resposta1 == "s":
                resposta1 = input(self.mensagem1)
                self.GerarValorDoDado()
                if resposta1 == "não" or resposta1 == "n":
                    print("Programa encerrado!")
            
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo)) # esse comando é uma forma de gerar valor mín/máx

# Para você usar uma classe você deve instânciar a mesma. Para fazer isso, segue abaixo:

simulador = SimuladorDeDado() 
simulador.Iniciar()
