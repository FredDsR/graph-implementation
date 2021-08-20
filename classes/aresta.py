from . import Nodo


class Aresta:
    def __init__(self, nodo_direito: Nodo,
                 nodo_esquerdo: Nodo, rotulo: str,
                 peso: float) -> None:
        self.nodo_direito = nodo_direito
        self.nodo_esquerdo = nodo_esquerdo
        self.rotulo = rotulo
        self.peso = peso

        self.nodo_direito.set_aresta(self)
        self.nodo_esquerdo.set_aresta(self)
