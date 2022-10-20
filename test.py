'''x = int(input("1 ou 2"))
if x == 1:
    nome = str(input("Digite o nome do paciente"))
    numero = int(input("Digite o numero do seu telefone"))
    data = str(input("Digite a data que sera a viagem"))
    local = str(input("Para onde sera a viagem"))
    consulta = str(input("O que fara no hospital?"))
    carro = str(input("Qual carro vai?"))
    informacoes = ("O nome do/a paciente é " + nome + "com numero de telefone" + telefone + " e na data "
                   + data + " ira para " + local + " para um/uma " + consulta + " com/no " + carro)
    print(informacoes)

if x == 2:
    nome = str(input("Digite seu Nome: "))
    carro = str(input("Qual carro dirige?: "))
    _RG = int(input("Digite seu RG(sem ponto ou traço)(para confirmação de identidade)"))
    informacoes = ("O nome do motorista é " + nome + " e ele dirige um/uma " + carro)
    print(informacoes)'''
from passageiro import Passageiros
from main import funcoes
from motorista import Motorista

passa = Passageiros('Esdras','12/2/12','fortaleza',85991577494)
fun = funcoes()
fun.cadastrar_passageiros(passa)
passa = Passageiros('Palo','12/3/12','algum Lugar',85921337494)
fun.cadastrar_passageiros(passa)
fun.print_passageiros()

motor = Motorista("Esda", "Busu", "Itapajé","Fortaleza")
fun.cadastrar_motorista(motor)
motor = Motorista("Poua", "carro Rapido", "Itapajé", "Sobral")
fun.cadastrar_motorista(motor)
fun.print_motorista()

