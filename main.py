import numpy as np
import grafos as gf
if __name__ == '__main__':
    x = 1
    dados = np.zeros((1,1))

    while x!=0:
        print("1 - Inserir vértice")
        print('2 - Inserir peso em um vértice')
        print('3 - Imprimir grafo (Matriz)')
        print('4 - Kruskal')
        print('0 - Sair')
        x = int(input('Digite a opção: '))
        if x==1:
            if len(dados)<20:
                dados = gf.inserir(dados)
            else:
                print('Número máximo atingido')
                print('Não é possível inserir mais vértices')
        elif x==2:
            dados = gf.manipula(dados)
        elif x==3:
            gf.imprimir(dados)
        elif x==4:
            gf.kruskal(dados)