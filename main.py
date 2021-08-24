from classes import Grafo

grafo = Grafo()
op = -1

while op != 0:
    print('-----------  Menu:  -----------')
    print('1 - Adicionar um vértice;')
    print('2 - Deletar um vértice;')
    print('3 - Ver vértices disponíveis;')
    print('4 - Adicionar uma aresta;')
    print('5 - Remover uma aresta;')
    print('6 - Ver grafo (lista encadeada);')
    print('7 - Gerar grafo de teste;')
    print('0 - Sair.')
    op = int(input('Digite uma das opções acima: '))

    if op == 1:
        # Adiciona vértice
        rotulo = input('Digite o rótulo do vértice: ')
        grafo.set_vertice(rotulo)
    elif op == 2:
        # Remove vértice
        rotulo = input('Digite o rótulo do vértice: ')
        grafo.delete_vertice(rotulo)
    elif op == 3:
        # Imprime vértices disponíveis
        grafo.print_vertices()
    elif op == 4:
        # Adiciona aresta
        rotulo_dir = input('Digite o rótulo do primeiro vértice: ')
        rotulo_esq = input('Digite o rótulo do segundo vértice: ')
        peso_aresta = float(input('Digite o peso da aresta (float): '))
        grafo.set_aresta(rotulo_dir, rotulo_esq, peso_aresta)
    elif op == 5:
        # Remove aresta
        rotulo_dir = input('Digite o rótulo do primeiro vértice: ')
        rotulo_esq = input('Digite o rótulo do segundo vértice: ')
        grafo.delete_aresta(rotulo_dir, rotulo_esq)
    elif op == 6:
        grafo.print_grafo()
    elif op == 7:
        grafo.criar_grafo_teste()
    elif op == 0:
        # Sai do programa
        print('Saindo...')
    else:
        # Entrada inválida
        print('Digite uma opção válida!')
