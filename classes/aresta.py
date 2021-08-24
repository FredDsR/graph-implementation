from . import Vertice


class Aresta:
    def __init__(self, vertice_direito: Vertice,
                 vertice_esquerdo: Vertice, rotulo: str,
                 peso: float) -> None:
        self.vertice_direito = vertice_direito
        self.vertice_esquerdo = vertice_esquerdo
        self.rotulo = rotulo
        self.peso = peso

        self.vertice_direito.set_aresta(self)
        self.vertice_esquerdo.set_aresta(self)

    def get_peso(self) -> float:
        return self.peso

    def set_peso(self, peso: float) -> None:
        self.peso = peso

    def delete_aresta(self) -> None:
        self.vertice_direito.remove_aresta(self)
        self.vertice_esquerdo.remove_aresta(self)
        del self
