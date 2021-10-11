import dijkstra as dj
import numpy as np
opcaoMenu = 1
#usa o numpy pra criar uma matriz vazia
dados = np.zeros(shape=(0,0))
while opcaoMenu!=0:
    count = len(dados) 
    print('Tamanho: {}'.format(count))
    print("1 - Inserir vértice")
    print('2 - Inserir peso em um vértice')
    print('3 - Imprimir grafo (Matriz)')
    print('4 - Dijkstra')
    print('0 - Sair')
    opcaoMenu = int(input('Digite a opção: '))
    if opcaoMenu==1:
        if count<20:
            dados = dj.inserir(dados)
        else:
            print('Número máximo atingido')
            print('Não é possível inserir mais vértices')
    elif opcaoMenu==2:
        dados = dj.manipula(dados)
    elif opcaoMenu==3:
        dj.imprimir(dados)
    elif opcaoMenu==4:
        dj.dijkstra(dados)