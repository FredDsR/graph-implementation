from classes import Grafo

grafo = Grafo()
op = ''

while op != '0':
    print('')
    print('-----------  Menu:  -----------')
    print('(1)  - Adicionar um vértice;')
    print('(2)  - Remover um vértice;')
    print('(3)  - Ver vértices disponíveis;')
    print('-------------------------------')
    print('(4)  - Adicionar uma aresta;')
    print('(5)  - Remover uma aresta;')
    print('-------------------------------')
    print('(6)  - Ver grafo (lista encadeada);')
    print('(7)  - Gerar grafo de teste;')
    print('-------------------------------')
    print('(8)  - Buscar menor caminho (Dijikstra);')
    print('(9)  - Gerar árvore mínima - inplace (Kruskal);')
    print('(10) - Gerar árvore máxima - inplace (Kruskal);')
    print('-------------------------------')
    print('(0)  - Sair.')
    op = input('Digite uma das opções acima: ')

    if op == '1':
        # Adiciona vértice
        rotulo = input('Digite o rótulo do vértice: ')
        print('')
        grafo.set_vertice(rotulo)
    elif op == '2':
        # Remove vértice
        rotulo = input('Digite o rótulo do vértice: ')
        print('')
        grafo.delete_vertice(rotulo)
    elif op == '3':
        # Imprime vértices disponíveis
        grafo.print_vertices()
        print('')
    elif op == '4':
        # Adiciona aresta
        rotulo_dir = input('Digite o rótulo do primeiro vértice: ')
        rotulo_esq = input('Digite o rótulo do segundo vértice: ')
        peso_aresta = float(input('Digite o peso da aresta (float): '))
        print('')
        grafo.set_aresta(rotulo_dir, rotulo_esq, peso_aresta)
    elif op == '5':
        # Remove aresta
        rotulo_dir = input('Digite o rótulo do primeiro vértice: ')
        rotulo_esq = input('Digite o rótulo do segundo vértice: ')
        print('')
        grafo.delete_aresta(rotulo_dir, rotulo_esq)
        print(f'Aresta entre {rotulo_dir} '
              f'e {rotulo_esq} removida com sucesso!')
    elif op == '6':
        # Imprime grafo na tela
        print('')
        grafo.print_grafo()
    elif op == '7':
        # Gera grafo para teste
        print('')
        grafo.criar_grafo_teste()
    elif op == '8':
        # Busca menor caminho
        rotulo_inicial = input('Digite o rótulo do vértice inicial: ')
        rotulo_final = input('Digite o rótulo do vértice final: ')
        print('')
        vertice_inicial = grafo.get_vertice(rotulo_inicial)
        vertice_final = grafo.get_vertice(rotulo_final)
        menor_caminho = grafo.menor_caminho_dijikstra(vertice_inicial,
                                                      vertice_final)
        if menor_caminho:
            grafo.print_caminho(menor_caminho)
    elif op == '9':
        # Gera árvore mínima
        print('')
        print('Árvore mínima:')
        grafo.gera_árvore_kruskal()
        grafo.print_grafo()
    elif op == '10':
        # Gera árvore máxima
        print('')
        print('Árvore máxima:')
        grafo.gera_árvore_kruskal(maxima=True)
        grafo.print_grafo()
    elif op == '0':
        # Sai do programa
        print('')
        print('Saindo...')
    else:
        # Entrada inválida
        print('')
        print('Digite uma opção válida!')
