from classes.aresta import Aresta


class Nodo:
    def __init__(self, rotulo: str) -> None:
        self.rotulo = rotulo
        self.arestas = []

    def set_aresta(self, aresta: Aresta):
        self.arestas.append(aresta)
