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
        print("Deseja tentar novamente?")
        print("0 - Sim")
        print("1 - Não")

        op = int(input("\nEscolha uma opção (0 ou 1): "))

        if op == 1:
            print("Encerrando o programa...")
            sys.exit()
