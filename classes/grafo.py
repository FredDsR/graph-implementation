import sys

from . import Vertice, Aresta


class Grafo:
    def __init__(self) -> None:
        self.limite_de_vertices = 20
        self.vertices = {}
        self.arestas = []

    def set_vertice(self, rotulo: str) -> None:

        if len(self.vertices) == self.limite_de_vertices:
            print(f'Limite de {self.limite_de_vertices} '
                  'vertices atingido.')
            return

        if self.existe_vertice(rotulo, show_message=False):
            print(f'Vertice {rotulo} já existe.')
            return

        self.vertices[rotulo] = Vertice(rotulo)
        print(f'Vértice {rotulo} criado com sucesso!')

    def get_vertice(self, rotulo) -> Vertice:
        if self.existe_vertice(rotulo):
            return self.vertices[rotulo]
        else:
            None

    def delete_vertice(self, rotulo: str) -> None:
        # ALERTA DE GAMBIARRA
        vertice = self.get_vertice(rotulo)
        if vertice:
            arestas = vertice.get_arestas()
            for i in range(len(arestas)):
                self.delete_aresta(arestas[0].get_vertice_direito(),
                                   arestas[0].get_vertice_esquerdo())
            self.vertices.pop(rotulo)
            del vertice

    def existe_vertice(self, rotulo: str, show_message: bool = True) -> bool:
        if rotulo not in self.vertices:
            if show_message:
                print(f'Vertice {rotulo} não existe!')
            return False
        else:
            return True

    def set_aresta(self, rotulo_vertice_dir: str, rotulo_vertice_esq: str,
                   peso: float) -> None:

        vertice_dir = self.get_vertice(rotulo_vertice_dir)
        vertice_esq = self.get_vertice(rotulo_vertice_esq)

        if vertice_esq and vertice_dir:
            new_aresta = Aresta(rotulo_vertice_dir,
                                rotulo_vertice_esq,
                                peso)

            vertice_dir.set_aresta(new_aresta)
            vertice_esq.set_aresta(new_aresta)

            self.arestas.append(new_aresta)

    def get_aresta(self, rotulo_vertice_dir: str,
                   rotulo_vertice_esq: str) -> Aresta:

        if (self.existe_vertice(rotulo_vertice_dir)
                and self.existe_vertice(rotulo_vertice_esq)):

            for aresta in self.arestas:

                rotulo_dir_aresta = aresta.get_vertice_direito()
                rotulo_esq_aresta = aresta.get_vertice_esquerdo()

                if (rotulo_vertice_dir == rotulo_dir_aresta
                    and rotulo_vertice_esq == rotulo_esq_aresta) \
                    or (rotulo_vertice_esq == rotulo_dir_aresta
                        and rotulo_vertice_dir == rotulo_esq_aresta):
                    return aresta
        return None

    def delete_aresta(self, rotulo_vertice_dir: str,
                      rotulo_vertice_esq: str) -> None:

        aresta_to_remove = self.get_aresta(rotulo_vertice_dir,
                                           rotulo_vertice_esq)

        print('Aresta to remove:', aresta_to_remove)
        if not aresta_to_remove:
            print(f'Não existe aresta entre {rotulo_vertice_dir} '
                  f'e {rotulo_vertice_esq}.')
            return

        vertice_dir = self.get_vertice(rotulo_vertice_dir)
        vertice_esq = self.get_vertice(rotulo_vertice_esq)

        vertice_dir.delete_aresta(aresta_to_remove)
        vertice_esq.delete_aresta(aresta_to_remove)

        self.arestas.remove(aresta_to_remove)

        print(f'Aresta entra {rotulo_vertice_dir} '
              f'e {rotulo_vertice_esq} removida com sucesso!')

        del aresta_to_remove

    def print_vertices(self) -> None:
        vertices = '; '.join(self.vertices.keys())
        print(f'Vértices disponíveis: {vertices};')

    def print_grafo(self) -> None:
        if len(self.vertices) == 0:
            print('Não existem vértices no grafo.')
            return

        print('----- Grafo: -----')
        for vertice in self.vertices:
            pesos = []
            rotulos = []
            rotulo_vertice = self.vertices[vertice].get_rotulo()

            for aresta in self.vertices[vertice].get_arestas():
                vdireito = aresta.get_vertice_direito()
                vesquerdo = aresta.get_vertice_esquerdo()
                peso = aresta.get_peso()
                pesos.append(peso)
                rotulos.append(vdireito) if vesquerdo == rotulo_vertice \
                    else rotulos.append(vesquerdo)
            labels = ' '.join([f'-- {peso} --> {vertice}'
                               for peso, vertice in zip(pesos, rotulos)])
            print(f'{rotulo_vertice} {labels}')

    def criar_grafo_teste(self) -> None:
        self.set_vertice('A')
        self.set_vertice('B')
        self.set_vertice('C')
        self.set_vertice('D')
        self.set_vertice('E')
        self.set_vertice('F')

        self.set_aresta('A', 'B', 10)
        self.set_aresta('A', 'D', 5)
        self.set_aresta('B', 'D', 3)
        self.set_aresta('B', 'C', 1)
        self.set_aresta('C', 'D', 8)
        self.set_aresta('C', 'E', 4)
        self.set_aresta('C', 'F', 4)
        self.set_aresta('D', 'E', 2)
        self.set_aresta('E', 'F', 6)

    def menor_caminho_dijikstra(self, vertice_inicial: Vertice,
                                vertice_final: Vertice) -> str:

        if not vertice_inicial or not vertice_final:
            return None

        rotulos = list(self.vertices.keys())
        aberto = [True] * len(rotulos)
        antecessores = [''] * len(rotulos)
        pesos = [sys.maxsize] * len(rotulos)

        idx_atual = rotulos.index(vertice_inicial.get_rotulo())
        pesos[idx_atual] = 0
        aberto[idx_atual] = False

        vertice_atual = vertice_inicial

        while any(aberto):
            arestas = vertice_atual.get_arestas()

            rotulo_mais_perto = ''
            menor_caminho = sys.maxsize

            for aresta in arestas:
                v_dir = aresta.get_vertice_direito()
                v_esq = aresta.get_vertice_esquerdo()

                rotulo_vizinho = v_dir if v_dir != vertice_atual.get_rotulo() \
                    else v_esq
                idx_vizinho = rotulos.index(rotulo_vizinho)

                if not aberto[idx_vizinho]:
                    continue

                peso = aresta.get_peso() + pesos[idx_atual]

                if pesos[idx_vizinho] > peso:

                    pesos[idx_vizinho] = peso
                    antecessores[idx_vizinho] = rotulos[idx_atual]

                    aberto[idx_vizinho] = False
                else:
                    peso = pesos[idx_vizinho]

                if peso < menor_caminho:
                    menor_caminho = peso
                    rotulo_mais_perto = rotulo_vizinho

            vertice_atual = self.get_vertice(rotulo_mais_perto)
            idx_atual = rotulos.index(rotulo_mais_perto)

        caminho = f'--> {vertice_final.get_rotulo()}'
        idx_atual = rotulos.index(vertice_final.get_rotulo())
        antecessor = antecessores[idx_atual]
        while antecessor != vertice_inicial.get_rotulo():
            caminho = f'--> {antecessor} --{pesos[idx_atual]}' + caminho
            idx_atual = rotulos.index(antecessor)
            antecessor = antecessores[idx_atual]

        caminho = antecessor + ' --' + str(pesos[idx_atual]) + caminho

        return caminho
