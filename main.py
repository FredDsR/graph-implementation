from classes import Grafo

grafo = Grafo()
op = -1

while op != 0:
    print('-----------  Menu:  -----------')
    print('1 - Adicionar um vértice;')
    print('2 - Deletar um vértice;')
    print('3 - Adicionar uma aresta;')
    print('4 - Remover uma aresta;')
    print('0 - Sair.')
    op = input('Digite uma das opções acima:')

    if op == 1:
        # Adiciona vértice
        rotulo = input('Digite o rótulo do vértice:')
        grafo.set_vertice(rotulo)
    elif op == 2:
        # Remove vértice
        rotulo = input('Digite o rótulo do vértice:')
        grafo.delete_vertice(rotulo)
    elif op == 3:
        # Adiciona aresta
        rotulo_dir = input('Digite o rótulo do primeiro vértice:')
        rotulo_esq = input('Digite o rótulo do segundo vértice:')
        rotulo_aresta = input('Digite o rótulo do vértice:')
        peso_aresta = float(input('Digite o peso do vértice (float):'))
        grafo.set_aresta(rotulo_dir, rotulo_esq, rotulo_aresta, peso_aresta)
    elif op == 4:
        # Remove aresta
        rotulo_dir = input('Digite o rótulo do primeiro vértice:')
        rotulo_esq = input('Digite o rótulo do segundo vértice:')
        grafo.delete_aresta(rotulo_dir, rotulo_esq)
    elif op == 0:
        # Sai do programa
        print('Saindo...')
    else:
        # Entrada inválida
        print('Digite uma opção válida!')
