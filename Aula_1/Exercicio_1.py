import Conversor


print("SISTEMA DE CONVERSÃO DE MEDIDAS ")
print("1 - Pé para Metros")
print("2 - Metros para Pé")
print("3 - Jarda para Metros")
print("4 - Jarda para Pé")



opcao = input("Escolha uma opção (1 a 4): ")


valor_usuario = float(input("Digite o valor que deseja converter: "))


if opcao == "1":
    resultado = Conversor.pes_para_metros(valor_usuario)
    print(f"\n{valor_usuario} pés equivalem a {resultado:.2f} metros.")

elif opcao == "2":
    resultado = Conversor.metros_para_pes(valor_usuario)
    print(f"\n{valor_usuario} metros equivalem a {resultado:.2f} pés.")

elif opcao == "3":
    resultado = Conversor.jarda_para_metros(valor_usuario)
    print(f"\n{valor_usuario} jardas equivalem a {resultado:.2f} metros.")

elif opcao == "4":
    resultado = Conversor.jarda_para_pes(valor_usuario)
    print(f"\n{valor_usuario} jardas equivalem a {resultado:.2f} pés.")

else:
    print("\nPor favor, rode o programa novamente e escolha de 1 a 4.")
