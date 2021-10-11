import numpy as np
def inserir(dados):
    #cria uma nova coluna
    dados = np.insert(dados, dados.shape[0], 0, axis=0)
    #cria uma nova linha
    dados = np.insert(dados, dados.shape[1], 0, axis=1)
    #insere o peso na coordenada 
    print('Vértice criado')
    return dados

def manipula(dados):
    imprimir(dados)
    x = int(input('Qual o índice da coluna: '))
    y = int(input('Qual o índice da linha: '))
    peso = float(input('Qual o peso desse vértice: '))
    #adiciona o peso numa coordenada já existente
    dados[y,x] = peso
    dados[x,y] = peso
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

def kruskal(dados):
    #vertices recebe [linha,coluna,peso]    
    vertices = ()
    for j in range(len(dados)):
        for i in range(len(dados)):
            if dados[j][i]!=0:
                vertices.append([j,i,dados[j][i]])
