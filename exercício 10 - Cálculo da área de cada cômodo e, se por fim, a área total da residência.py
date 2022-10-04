"""
Escrever um programa que possibilite calcular a área total em metros de uma residência com cômodos sala, cozinha,
banheiro, dois quartos, área de serviço, quintal, garagem, entre outros que podem ser fornecidos ao programa. 
O programa deve solicitar a entrada do nome, da largura e do comprimento de um determinado cômodo. Em seguida, 
deve apresentar a área do cômodo lido e também uma mensagem solicitando ao usuário a confirmação de continuar 
calculando novos cômodos. Caso o usuário responda "NÃO", o programa deve apresentar o valor total acumulado da 
área residencial.

"""
q = 0 
area = 0 
resposta = "sim"


while resposta == str("sim"):
    comodo = str(input(f"\nDigite o cômodo que deve ser calculado: "))
    largura = float(input(f"\nDigite a largura do {comodo}: "))
    comprimento = float(input(f"Digite o comprimento do {comodo}: "))

    area = largura * comprimento
        
    print(f"\nA área do {comodo} corresponde à: {area} m².")
    
    q = area + q

    resposta = str(input("Deseja continuar calculando novos cômodos? "))
    if resposta == str("não"):
        print(f"\nO total da área residencial é: {q} m².\n")


