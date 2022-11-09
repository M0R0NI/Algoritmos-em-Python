import random
import time

def pesquisa_sequencial(l, alvo):
    for i in range(len(l)):
        if l[i] == alvo:
            return i
    return - 1

def pesquisa_binaria(l, alvo, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1 
    
    if high < low:
        return -1
    ponto_medio = (low + high) // 2 

    if l[ponto_medio] == alvo:
        return ponto_medio
    elif alvo < l[ponto_medio]:
        return pesquisa_binaria(l, alvo, low, ponto_medio-1)
    else:
        return pesquisa_binaria(l, alvo, ponto_medio+1, high)

if __name__=='__main__':
    #l = [1, 3, 5, 10, 12]
    #alvo = 10
    #print(pesquisa_sequencial(l, alvo))
    #print(pesquisa_binaria(l, alvo))

    length = 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for alvo in sorted_list:
        pesquisa_sequencial(sorted_list, alvo)
    end = time.time()
    print("Tempo de busca sequencial: ", (end - start)/length, "segundos")

    start = time.time()
    for alvo in sorted_list:
        pesquisa_binaria(sorted_list, alvo)
    end = time.time()
    print("Tempo de busca binária: ", (end - start)/length, "segundos")
