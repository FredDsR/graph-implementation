from . import Vertice, Aresta


class Grafo:
    def __init__(self) -> None:
        self.limite_de_vertices = 20
        self.vertices = {}
        self.arestas = []

    def set_vertice(self, rotulo: str, replace: bool = False) -> None:

        if len(self.vertices) == self.limite_de_vertices:
            raise Exception(f'Limite de {self.limite_de_vertices} '
                            'vertices atingido.')

        if self.existe_vertice(rotulo) and not replace:
            raise Exception(f'Error: Vertice {rotulo} já existe.')

        self.vertices[rotulo] = Vertice(rotulo)

    def get_vertice(self, rotulo) -> Vertice:
        if self.existe_vertice(rotulo, raise_error=True):
            return self.vertices[rotulo]
        else:
            None

    def delete_vertice(self, rotulo: str) -> None:
        if self.existe_vertice(rotulo):
            vertice = self.vertices.pop(rotulo)
            vertice.reset_arestas()
            del vertice

    def existe_vertice(self, rotulo: str, raise_error: bool = False) -> bool:
        if rotulo not in self.vertices:
            if raise_error:
                raise Exception(f'Error: Vertice {rotulo} '
                                'não encontrado.')
            else:
                return False
        else:
            return True

    def set_aresta(self, rotulo_vertice_dir: str, rotulo_vertice_esq: str,
                   peso: float) -> None:

        vertice_dir = self.get_vertice(rotulo_vertice_dir)
        vertice_esq = self.get_vertice(rotulo_vertice_esq)

        new_aresta = Aresta(rotulo_vertice_dir,
                            rotulo_vertice_esq,
                            peso)

        vertice_dir.set_aresta(new_aresta)
        vertice_esq.set_aresta(new_aresta)

        self.arestas.append(new_aresta)

    def get_aresta(self, rotulo_vertice_dir: str,
                   rotulo_vertice_esq: str) -> Aresta:
        vertice_dir = self.get_vertice(rotulo_vertice_dir)
        vertice_esq = self.get_vertice(rotulo_vertice_esq)

        for varesta in self.arestas:
            vertice_dir_aresta = varesta.get_vertice_direito()
            vertice_esq_aresta = varesta.get_vertice_esquerdo()

            if (vertice_dir is vertice_dir_aresta
                and vertice_esq is vertice_esq_aresta) \
                or (vertice_esq is vertice_dir_aresta
                    and vertice_dir is vertice_esq_aresta):
                return varesta
        return None

    def delete_aresta(self, rotulo_vertice_dir: str,
                      rotulo_vertice_esq: str) -> None:

        # TODO ta rolando alguma merda aqui, não ta deletado

        aresta_to_remove = self.get_aresta(rotulo_vertice_dir,
                                           rotulo_vertice_esq)
        vertice_dir = self.get_vertice(rotulo_vertice_dir)
        vertice_esq = self.get_vertice(rotulo_vertice_esq)

        vertice_dir.delete_aresta(aresta_to_remove)
        vertice_esq.delete_aresta(aresta_to_remove)

        self.arestas = [aresta if aresta is not aresta_to_remove
                        else aresta for aresta in self.arestas]

        del aresta_to_remove

    def print_vertices(self) -> None:
        vertices = '; '.join(self.vertices.keys())
        print(f'Vértices disponíveis: {vertices};')
        print('')

    def print_grafo(self) -> None:
        print('Grafo:')
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
        self.set_vertice('Pel')
        self.set_vertice('Poa')
        self.set_vertice('Bage')
        self.set_vertice('Chui')

        self.set_aresta('Pel', 'Poa', 150.8)
        self.set_aresta('Pel', 'Chui', 40.7)
        self.set_aresta('Poa', 'Bage', 78.3)
        self.set_aresta('Chui', 'Bage', 55.2)
        self.set_aresta('Bage', 'Pel', 15.5)
