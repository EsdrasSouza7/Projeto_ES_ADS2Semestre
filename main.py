from login import LoginMotor, LoginPassa

class funcoes:
    def __init__(self):
        self.loginPassageiros = []
        self.loginMotoristas = []

    #O cliente vai se cadastrar sem escolher o carro? sim. Deverá selecionar os Horarios disponiveis.
    #Notificar o cliente com antecedencia sobre o horario marcado.
    def cadastrar_passageiros(self,passageiros: LoginPassa):
        self.loginPassageiros.append(passageiros)

    def cadastrar_motorista(self,motor: LoginMotor):
        self.loginMotoristas.append(motor)

    def print_passageiros(self):
        i = 1
        for passageiros in self.loginPassageiros:
            passa = passageiros.get_passageiro()
            print("Nº" + str(i) + " | Nome:" + passa.Nome + " | Destino:" + passa.local + " | Telefone:" + str(passa.telefone))
            i+=1

    def print_motorista(self):
        i = 1
        for motorista in self.loginMotoristas:
            motor = motorista.get_motorista()
            print("Nº" + str(i) + " | Nome:" + motor.Nome + " | Carro:" + motor.carro + " | Rota:" + motor.destinoIni + "-" + motor.destinoFin)
            i+=1

    def loggando(self, nickname, senha, passaMotor):
        if passaMotor == 1:
            for passa in self.loginPassageiros:
                test = passa.verificacao(nickname, senha)
                if test != None:
                    return test
            print("Login ou Senha Errada")
            return None
        elif passaMotor == 2:
            for motor in self.loginMotoristas:
                test = motor.verificacao(nickname, senha)
                if test != None:
                    return test
            print("Login ou Senha Errada")
            return None
        else:
            print("Erro: opção desconhecida")
            return None