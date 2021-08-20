from classes import Nodo, Aresta

op = -1
matriz_adjacencia = []

# TODO utilizar classe Grafo para manipulações

def addNodo():
    rotulo = input('Digite o rótulo do novo nodo:')

    novo_nodo = Nodo(rotulo)

    if len(matriz_adjacencia) > 0:
        nodo


while op != 0:
    print('-----------  Menu:  -----------')
    print('1 - Adicionar um nodo;')
    print('2 - Deletar um nodo;')
    print('3 - Imprimir matriz de adjacência;')
    print('0 - Sair')
    op = input('Digite uma das opções acima:')

    if op == 1:
        addNodo()
