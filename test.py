from passageiro import Passageiros
from main import funcoes
from motorista import Motorista
from login import LoginMotor, LoginPassa

#criação da função
fun = funcoes()
print("Teste de criação dos passageiros")
passa = Passageiros('Esdras','12/2/12','fortaleza',85991577494)
login = LoginPassa("sete", "12345", passa)
fun.cadastrar_passageiros(login)
passa = Passageiros('Paulo','16/1/09','Sobral',85991545494)
login = LoginPassa("paulo", "12345", passa)
fun.cadastrar_passageiros(login)
fun.print_passageiros()

print("")
print("Teste de criação de motorista")
motor = Motorista("Esda", "Busu", "Itapajé","Fortaleza")
login = LoginMotor("motorista1", "54321", motor)
fun.cadastrar_motorista(login)  #Colocar um modo de verificar se ja existe nickname
motor = Motorista("Poua", "carro Rapido", "Itapajé", "Sobral")
login = LoginMotor("motorista2", "1234", motor) # nao ter dois nickname iguais
fun.cadastrar_motorista(login)
fun.print_motorista()

print("")
print("Teste de login")
print(fun.loggando("paulo", "12345", 1)) #certo
print(fun.loggando("motorista2", "1234", 2)) #certo
print(fun.loggando("motorista1", "123", 2)) #Erro na senha
print(fun.loggando("seee", "12345", 1)) #Erro no Nickname/e-mail



#while True::
 #   print("O que Gostaria de fazer?")
  #  print("1 - Login  2 - cadastro")
   # input(int("R: "))

#x = int(input("1 ou 2"))
#if x == 1:
 #   nome = str(input("Digite o nome do paciente"))
  #  numero = int(input("Digite o numero do seu telefone"))
   # data = str(input("Digite a data que sera a viagem"))
    #local = str(input("Para onde sera a viagem"))
#    consulta = str(input("O que fara no hospital?"))
 #   carro = str(input("Qual carro vai?"))
  #  informacoes = ("O nome do/a paciente é " + nome + "com numero de telefone" + telefone + " e na data "
   #                + data + " ira para " + local + " para um/uma " + consulta + " com/no " + carro)
    #print(informacoes)

#if x == 2:
 #   nome = str(input("Digite seu Nome: "))
 #  carro = str(input("Qual carro dirige?: "))
  # _RG = int(input("Digite seu RG(sem ponto ou traço)(para confirmação de identidade)"))
   # informacoes = ("O nome do motorista é " + nome + " e ele dirige um/uma " + carro)
#    print(informacoes)'''