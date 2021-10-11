import numpy as np
caminho = [] 
pendentes = [] 
vistos = []     
def dijkstra(dados):
    imprimir(dados)
    #contem o caminho mais curto
    caminho = []
    #contem os que estão para análise
    pendentes = [] 
    #contem os que já foram analisados, resultado de tudo
    vistos = []  
    algoritmo(dados)
    
def algoritmo(dados):

    print('Digite a linha do vértice origem')
    print('Ex: se o primeiro vértice é o 0, digite 0')
    l = int(input("Valor: "))
    caminho = [] 
    pendentes = [] 
    vistos = []  
    #usado pra controlar o laço 
    i=0
    count = 0
    indiceAux = 0
    #pendentes recebe a origem
    pendentes.append(l)
    #já vistos recebe a origem
    #formato: [vértice atual, peso, vértice anterior]
    #a origem recebe -1 como vértice anterior pra dizer que este não existe
    vistos.append([l,0,-1])
    while i<len(dados):
        count = 0
        #usado pra percorrer a linha/vizinhos
        if dados[pendentes[0]][i]>0:
            #se o peso for maior que 0, vai pra análise
            var = analise(i)
            if var == 0:
                #se ele não foi analisado ainda, é incluido na lista pendentes
                pendentes.append(i)
            for j in range(len(vistos)):
                #percorre a lista dos que já foram vistos
                if vistos[j][0] == i:
                    indiceAux = j
                    count+=1
                #se o elemento em vistos é o primeiro de pendentes, atualiza o índice
                if vistos[j][0] == pendentes[0]:
                    indiceVisitante = j
            if count == 0:
                #se não há elementos, insere no vistos
                #vistos recebe (indice,valor,anterior)
                vistos.append([i,vistos[indiceVisitante][1]+dados[pendentes[0]][i],pendentes[0]])
            else:
                #se o caminho existente é maior que o caminho sendo analisado
                if vistos[indiceAux][1] > vistos[indiceVisitante][1]+dados[pendentes[0]][i]:
                    #insere o caminho que fora analisado; o menor
                    vistos[indiceAux][1] = vistos[indiceVisitante][1]+dados[pendentes[0]][i]
                    vistos[indiceAux][2] = pendentes[0]
        #se chegou ao limite da linha
        if i+1 == len(dados):
            #insere no caminho o primeiro de pendentes
            caminho.append(pendentes[0])
            #remove ele de pendentes
            pendentes.pop(0)
            #se ainda houver pendentes, reinicia
            if len(pendentes)>0:
                i=0
            else:
                break
        else:
            i+=1
    if len(dados)>0:
        print("Aqui será exibido o menor caminho possível para determinado vértice")
        print('seguido de seu valor, e o vértice anterior para chegar a ele')
        print("O vértice origem irá conter '-1' para sinalizar que não há anterior")
        print('Vértice Destino\t-\tGasto total\t-\tVértice Anterior\t-')
        for i in range(len(vistos)):
            for j in range(3):
                print(vistos[i][j],end='\t\t-\t')
            print('\n')
    else:
        print('Não foi encontrado vértices')
            
            
def analise(indice):
    #retorna diferente de 0 se este está em pendentes ou caminho
    #ou seja, já foi alvo 
    contador=0
    for i in range(len(pendentes)):
        if indice in pendentes:
            contador+=1
    for i in range(len(caminho)):
        if indice in caminho:
            contador+=1
    return contador


def inserir(dados):
    #insere linhas e colunas na matriz
    print("Criando vértice")
    #cria linha e insere os valores 0 
    dados = np.insert(dados, dados.shape[0], 0, axis=0)
    #cria coluna e insere os valores 0
    dados = np.insert(dados, dados.shape[1], 0, axis=1)
    return dados 

def imprimir(dados):
    #imprime a matriz
    print('Imprimindo')
    print(0,end='\t')
    for i in range(len(dados)):
        print(i, end='\t')
    print('\n')
    for i in range(len(dados)):
        print(i, end = '\t')
        for j in range(len(dados)):
            print(dados[i][j], end = '\t')
        print('\n')

def manipula(dados):
    #insere o valor do vértice na coordenada linhaXcoluna
    imprimir(dados)
    col = int(input('Digite o índice da coluna: '))
    linha = int(input('Digite o índice da linha: '))
    valor = float(input('Digite o valor do vértice: '))
    if col == linha:
        print('Distancia entre ele mesmo só pode ser zero')
        valor = 0
    dados[linha][col] = valor
    return dados