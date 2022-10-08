"""
Elaborar um programa que calcule e apresente o valor da média geral das médias individuais de uma classe com oito alunos.

"""
q = 1
soma = 0

q1 = 1
soma1 = 0

q2 = 1
soma2 = 0 

q3 = 1
soma3 = 0 

media_geral = 0 

while q <= 4:
    notas = int(input("Digite a sua nota: "))
    soma = notas + soma
    media = soma / q 
    q = q + 1

    if q == 5:
        print(f"média Aluno 1: {media}\n")

while q1 <= 4:
    notas1 = int(input("Digite a sua nota: "))
    soma1 = notas1 + soma1
    media1 = soma1 / q1 
    q1 = q1 + 1
 
    if q1 == 5:
        print(f"média Aluno 2: {media1}\n")

while q2 <= 4:
    notas2 = int(input("Digite a sua nota: "))
    soma2 = notas2 + soma2
    media2 = soma2 / q2 
    q2 = q2 + 1
 
    if q2 ==5:
     print(f"média Aluno 3: {media2}\n")        

while q3 <= 4:
    notas3 = int(input("Digite a sua nota: "))
    soma3 = notas3 + soma3
    media3 = soma3 / q3 
    q3 = q3 + 1
   
    if q3 == 5:
        print(f"média Aluno 4: {media3}\n")

media_geral = (media + media1 + media2 + media3) / 4
print(f"A média geral é: {media_geral}")

    
