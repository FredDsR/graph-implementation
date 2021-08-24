
class Aresta:
    def __init__(self, rotulo_vertice_direito: str,
                 rotulo_vertice_esquerdo: str, peso: float) -> None:
        self.rotulo_vertice_direito = rotulo_vertice_direito
        self.rotulo_vertice_esquerdo = rotulo_vertice_esquerdo
        self.peso = peso

    def get_peso(self) -> float:
        return self.peso

    def set_peso(self, peso: float) -> None:
        self.peso = peso

    def get_vertice_direito(self) -> str:
        return self.rotulo_vertice_direito

    def get_vertice_esquerdo(self) -> str:
        return self.rotulo_vertice_esquerdo
