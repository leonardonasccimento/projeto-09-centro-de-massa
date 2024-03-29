import os

coordenadasDosCorpos = []
massasDosCorpos = []
numeroDeDimensoes = 0
numeroDeCorpos = 0

def calcularCoordenadas(
    coordenadasDosCorpos, massasDosCorpos, numeroDeDimensoes, numeroDeCorpos
):

    print()
    for dimensoes in range(1, numeroDeDimensoes + 1):
        for corpos in range(1, numeroDeCorpos + 1):
            valoresDasDimensoes = int(
                input(f"Digite a {dimensoes}ª coordenada do corpo {corpos}: ")
            )
            coordenadasDosCorpos.append(valoresDasDimensoes)

    print()
    for massas in range(0, numeroDeCorpos):
        valoresDasMassasDosCorpos = float(
            input(f"Digite o valor da massa do corpo {massas+1}: ")
        )
        massasDosCorpos.append(valoresDasMassasDosCorpos)

    print()
    somaDasMassas = sum(massasDosCorpos)
    numeroDeCoordenadas = len(coordenadasDosCorpos)
    numeradorDaCoordenada = 0
    for massas in range(1, numeroDeCorpos + 1):
        for coordenadas in range(1, numeroDeCoordenadas + 1):
            if massas == coordenadas:
                numeradorDaCoordenada += (
                    massasDosCorpos[massas - 1] * coordenadasDosCorpos[coordenadas - 1]
                )
    
    coordenada = numeradorDaCoordenada / somaDasMassas
    print(f"1ª coordenada do centro de massa do(s) corpo(s) = {round(coordenada,4)}")

    if numeroDeDimensoes < 2:
        return

    numeradorDaCoordenada = 0
    for massas in range(1, numeroDeCorpos + 1):
        for coordenadas in range(1, numeroDeCoordenadas + 1):
            if coordenadas - massas == numeroDeCorpos:
                numeradorDaCoordenada += (
                    massasDosCorpos[massas - 1] * coordenadasDosCorpos[coordenadas - 1]
                )

    coordenada = numeradorDaCoordenada / somaDasMassas
    print(f"2ª coordenada do centro de massa do(s) corpo(s) = {round(coordenada,4)}")

    if numeroDeDimensoes < 3:
        return

    numeradorDaCoordenada = 0
    for massas in range(1, numeroDeCorpos + 1):
        for coordenadas in range(1, numeroDeCoordenadas + 1):
            if coordenadas - massas == numeroDeCorpos * 2:
                numeradorDaCoordenada += (
                    massasDosCorpos[massas - 1] * coordenadasDosCorpos[coordenadas - 1]
                )

    coordenada = numeradorDaCoordenada / somaDasMassas
    print(f"3ª coordenada do centro de massa do(s) corpo(s) = {round(coordenada,4)}")

    if numeroDeDimensoes < 4:
        return

    numeradorDaCoordenada = 0
    for massas in range(1, numeroDeCorpos + 1):
        for coordenadas in range(1, numeroDeCoordenadas + 1):
            if coordenadas - massas == numeroDeCorpos * 3:
                numeradorDaCoordenada += (
                    massasDosCorpos[massas - 1] * coordenadasDosCorpos[coordenadas - 1]
                )

    coordenada = numeradorDaCoordenada / somaDasMassas
    print(f"4ª coordenada do centro de massa do(s) corpo(s) = {round(coordenada,4)}")

    if numeroDeDimensoes < 5:
        return

    numeradorDaCoordenada = 0
    for massas in range(1, numeroDeCorpos + 1):
        for coordenadas in range(1, numeroDeCoordenadas + 1):
            if coordenadas - massas == numeroDeCorpos * 4:
                numeradorDaCoordenada += (
                    massasDosCorpos[massas - 1] * coordenadasDosCorpos[coordenadas - 1]
                )

    coordenada = numeradorDaCoordenada / somaDasMassas
    print(f"5ª coordenada do centro de massa do(s) corpo(s) = {round(coordenada,4)}")


while True:
    opcao = int(
        input(
            "Digite uma opção e prima Enter: \n (9) para calcular centro de massa  \n (8) para sair: "
        )
    )
    print()

    if opcao == 8:
        exit(0)

    numeroDeDimensoes = int(input("Digite o número de dimensões do sistema: "))
    numeroDeCorpos = int(input("Digite o número de corpos do sistema: "))

    if numeroDeDimensoes <= 5 and numeroDeDimensoes > 0:
        calcularCoordenadas(
            coordenadasDosCorpos, massasDosCorpos, numeroDeDimensoes, numeroDeCorpos
        )
    else:
        print(f"\nO número de dimensões deve ser maior do que 0 e menor do que 6.")

    print()
    parada = int(input("Digite (9) para sair ou digite (8) para um novo cálculo: "))
    if parada == 9:
        break
    print()
