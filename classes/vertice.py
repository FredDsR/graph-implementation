from .aresta import Aresta


class Vertice:
    def __init__(self, rotulo: str) -> None:
        self.rotulo = rotulo
        self.arestas = []

    def set_aresta(self, aresta: Aresta) -> None:
        self.arestas.append(aresta)

    def delete_aresta(self, aresta_to_remove: Aresta) -> None:

        self.arestas.remove(aresta_to_remove)

    def get_arestas(self) -> list:
        return self.arestas

    def get_rotulo(self) -> str:
        return self.rotulo
