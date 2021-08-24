from .aresta import Aresta


class Vertice:
    def __init__(self, rotulo: str) -> None:
        self.rotulo = rotulo
        self.arestas = []

    def set_aresta(self, aresta: Aresta) -> None:
        self.arestas.append(aresta)

    def delete_aresta(self, aresta_to_remove: Aresta) -> None:
        self.arestas = [aresta if aresta is not aresta_to_remove
                        else aresta for aresta in self.arestas]

    def reset_arestas(self) -> None:
        for aresta in self.arestas:
            self.delete_aresta(aresta)

    def get_arestas(self) -> list:
        return self.arestas

    def get_rotulo(self) -> str:
        return self.rotulo
