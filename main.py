from classes import Grafo

grafo = Grafo()
op = -1

while op != 0:
    print('')
    print('-----------  Menu:  -----------')
    print('(1) - Adicionar um vértice;')
    print('(2) - Remover um vértice;')
    print('(3) - Ver vértices disponíveis;')
    print('-------------------------------')
    print('(4) - Adicionar uma aresta;')
    print('(5) - Remover uma aresta;')
    print('-------------------------------')
    print('(6) - Ver grafo (lista encadeada);')
    print('(7) - Gerar grafo de teste;')
    print('-------------------------------')
    print('(0) - Sair.')
    op = int(input('Digite uma das opções acima: '))

    if op == 1:
        # Adiciona vértice
        rotulo = input('Digite o rótulo do vértice: ')
        print('')
        grafo.set_vertice(rotulo)
    elif op == 2:
        # Remove vértice
        rotulo = input('Digite o rótulo do vértice: ')
        print('')
        grafo.delete_vertice(rotulo)
    elif op == 3:
        # Imprime vértices disponíveis
        grafo.print_vertices()
        print('')
    elif op == 4:
        # Adiciona aresta
        rotulo_dir = input('Digite o rótulo do primeiro vértice: ')
        rotulo_esq = input('Digite o rótulo do segundo vértice: ')
        peso_aresta = float(input('Digite o peso da aresta (float): '))
        print('')
        grafo.set_aresta(rotulo_dir, rotulo_esq, peso_aresta)
    elif op == 5:
        # Remove aresta
        rotulo_dir = input('Digite o rótulo do primeiro vértice: ')
        rotulo_esq = input('Digite o rótulo do segundo vértice: ')
        print('')
        grafo.delete_aresta(rotulo_dir, rotulo_esq)
    elif op == 6:
        # Imprime grafo na tela
        print('')
        grafo.print_grafo()
    elif op == 7:
        # Gera grafo para teste
        print('')
        grafo.criar_grafo_teste()
    elif op == 0:
        # Sai do programa
        print('')
        print('Saindo...')
    else:
        # Entrada inválida
        print('')
        print('Digite uma opção válida!')
