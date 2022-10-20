from passageiro import Passageiros
from motorista import Motorista

class funcoes:
    def __init__(self):
        self.passageiros = []
        self.motoristas = []

    #O cliente vai se cadastrar sem escolher o carro? sim ou nao?
    def cadastrar_passageiros(self,passageiros: Passageiros):
        self.passageiros.append(passageiros)

    def cadastrar_motorista(self,motor: Motorista):
        self.motoristas.append(motor)

    def print_passageiros(self):
        i = 1
        for passageiros in self.passageiros:
            print("Nº" + str(i) + " | Nome:" + passageiros.Nome + " | Destino:" + passageiros.local + " | Telefone:" + str(passageiros.telefone))
            i+=1

    def print_motorista(self):
        i = 1
        for motor in self.motoristas:
            print("Nº" + str(i) + " | Nome:" + motor.Nome + " | Carro:" + motor.carro + " | Rota:" + motor.destinoIni + "-" + motor.destinoFin)
            i+=1

    #Linha 9 - Se sim Notificar o paciente quando o carro for selecionado para ela
    #Talvez fazer um selecionador automatico usando o distino do paciente e o desrino final do motorista