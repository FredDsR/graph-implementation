from . import Vertice, Aresta


class Grafo:
    def __init__(self) -> None:
        self.limite_de_vertices = 20
        self.vertices = {}
        self.matriz_adj = {}

    def set_vertice(self, rotulo: str, replace: bool = False) -> None:

        if len(self.vertices) == self.limite_de_vertices:
            raise Exception(f'Limite de {self.limite_de_vertices} '
                            'vertices atingido.')

        if self.existe_vertice and replace:
            raise Exception(f'Error: Vertice {rotulo} já existe.')

        self.vertices[rotulo] = Vertice(rotulo)

    def delete_vertice(self, rotulo: str) -> None:
        if self.existe_vertice(rotulo):
            vertice = self.vertices.pop(rotulo)
            vertice.delete_all_arestas()
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

    def get_vertice(self, rotulo) -> Vertice:
        if self.existe_vertice(rotulo, raise_error=True):
            return self.vertices[rotulo]

    def set_aresta(self, rotulo_vertice_dir: str, rotulo_vertice_esq: str,
                   rotulo_aresta: str, peso: float) -> None:

        self.existe_vertice(rotulo_vertice_dir, raise_error=True)
        self.existe_vertice(rotulo_vertice_esq, raise_error=True)

        Aresta(self.vertices[rotulo_vertice_dir],
               self.vertices[rotulo_vertice_esq],
               rotulo_aresta, peso)

    def delete_aresta(self, rotulo_vertice_dir: str,
                      rotulo_vertice_esq: str) -> None:
        # TODO Implementar função delete_aresta
        pass
