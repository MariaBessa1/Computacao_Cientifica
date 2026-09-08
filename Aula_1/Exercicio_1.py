import sys
import Conversor


def tela():
    print("\nSISTEMA DE CONVERSÃO DE MEDIDAS")
    print("1 - Pé para Metros")
    print("2 - Metros para Pé")
    print("3 - Jarda para Metros")
    print("4 - Jarda para Pé")


while True:
    tela()
    opcao = int(input("Escolha uma opção (1 a 4):\n"))

    if 1 <= opcao <= 4:
        valor = float(input("Digite o valor que deseja converter: "))
        Conversor.opcoes_de_conversao(opcao, valor)
        break

    else:
        print("\nPor favor, escolha uma opção válida de 1 a 4.")
        print("Deseja rodar novamente seu analfabeto?")
        print("0 - Sim, vou ler dessa vez e escolher uma das opções.")
        print("1 - Não, só queria ver se o programa reconhecia gente idiota.")

        op = int(input("\nEscolha uma opção (0 ou 1 seu animal): "))

        if op == 1:
            print("Encerrando o programa...")
            sys.exit()
