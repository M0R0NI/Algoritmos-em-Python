"""
Elaborar um programa que calcule e apresente o valor da média geral das médias individuais de uma classe com cinco alunos.

Aluno A média = 7
Aluno B média = 7.0
Aluno C média = 4
Aluno D média = 6.0
Aluno E média = 8
"""
media_individual = [7, 7, 4, 6, 8]
for media in media_individual:
    soma_media = sum(media_individual) # Para somar uma lista em Python usa-se a função 'sum()'.
    media_geral = soma_media / 5
    print(f"A média geral é: {media_geral}")
    






