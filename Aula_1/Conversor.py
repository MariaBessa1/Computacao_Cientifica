def opcoes_de_conversao(opcao, valor):
    match opcao:
        case 1:
            print(f"\n{valor} pés equivalem a {valor / 3.28084:.2f} metros.")
        case 2:
            print(f"\n{valor} metros equivalem a {valor * 3.28084:.2f} pés.")
        case 3:
            print(f"\n{valor} jardas equivalem a {valor * 0.9144:.2f} metros.")
        case 4:
            print(f"\n{valor} jardas equivalem a {valor * 3:.2f} pés.")
