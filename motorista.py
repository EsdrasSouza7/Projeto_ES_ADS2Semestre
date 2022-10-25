class Motorista:
    def __init__(self, nome, carro, distIni, distFin):
        self.Nome = nome
        self.carro = carro
        self.destinoIni = distIni
        self.destinoFin = distFin

    def set_distinoFinal(self, distFin):
        self.destinoFin = distFin

    def set_distinoInicial(self, distIni):
        self.destinoIni = distIni
