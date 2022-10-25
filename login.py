from passageiro import Passageiros
from motorista import Motorista

class LoginPassa:
    def __init__(self, nickname, senha, passageiro: Passageiros):
        self.nick = nickname
        self._senha = senha
        self.passageiro = passageiro

    def get_passageiro(self):
        return self.passageiro

    def verificacao(self, nickname, senha):
        if nickname == self.nick and senha == self._senha:
            return self.passageiro
        else:
            return None



class LoginMotor:
    def __init__(self, nickname, senha, motorista: Motorista):
        self.nick = nickname
        self._senha = senha
        self.motorista = motorista

    def get_motorista(self):
        return self.motorista

    def verificacao(self, nickname, senha):
        if nickname == self.nick and senha == self._senha:
            return self.motorista
        else:
            return None
