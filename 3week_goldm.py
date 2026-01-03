print("Olá este programa é um economista!")
print("Escolha uma das opções abaixo:" )
print("1-Câmbio de moedas")
print("2- Estabelecer relações entre moedas ")
print("3-É suficiente para comprar um big mac?")
print("4-Receber dinheiro dia sim dia não")
print("5- sair")

if str(input()) == "1":
    print("Converter de:")
    print("1- EUR")
    print("2-USD")
    print("3-BRL")
    moeda = int(input())
    print("Insira o valor a converter:")
    quant = float(input())
    print("A que moeda deseja converter?")
    print("1-EUR")
    print("2-USD")
    print("3-BRL")
    moeda_conv = int(input())
    if moeda == 1:
        if moeda_conv == 2:
            print(quant * 1.17, "USD")
        elif moeda_conv == 3:
            print(quant * 6.37, "BRL")
        else:
            print(quant)
    elif moeda == 2:
        if moeda_conv == 1:
            print(quant * 0.85, "EUR")
        elif moeda_conv == 3:
            print(quant * 5.44, "BRL")
        else:
            print(quant)
    elif moeda == 3:
        if moeda_conv == 1:
            print(quant * 0.16, "EUR")
        elif moeda_conv == 2:
            print(quant * 0.18, "USD")
        else:
            print(quant)
    if quant <= 0:
        print("Quantia inválida.")

if str(input()) == "2":
    print("Comparar duas quantias entre moedas")
    print("Moeda da primeira quantia:")
    print("1- EUR")
    print("2- USD")
    print("3- BRL")
    moeda1 = int(input())
    print("Insira a primeira quantia:")
    quant1 = float(input())
    print("Moeda da segunda quantia:")
    print("1- EUR")
    print("2- USD")
    print("3- BRL")
    moeda2 = int(input())
    print("Insira a segunda quantia:")
    quant2 = float(input())

    if moeda1 == 1:
        q1_eur = quant1
    elif moeda1 == 2:
        q1_eur = quant1 * 0.85
    else:
        q1_eur = quant1 * 0.16

    if moeda2 == 1:
        q2_eur = quant2
    elif moeda2 == 2:
        q2_eur = quant2 * 0.85
    else:
        q2_eur = quant2 * 0.16

    label1 = "EUR" if moeda1 == 1 else ("USD" if moeda1 == 2 else "BRL")
    label2 = "EUR" if moeda2 == 1 else ("USD" if moeda2 == 2 else "BRL")
    if q1_eur > q2_eur:
        print(f"{quant1} {label1} > {quant2} {label2}")
    elif q1_eur < q2_eur:
        print(f"{quant1} {label1} < {quant2} {label2}")
    else:
        print(f"{quant1} {label1} = {quant2} {label2} (aprox.)")
    if quant1 or quant2 <= 0:
        print("Quantia inválida.")

if str(input()) == "3":
    print("Qual a moeda que vais utilizar:")
    print("1- EUR")
    print("2- USD")
    print("3- BRL")
    moeda = int(input())
    print("Insira a sua quantia:")
    quant = float(input())
    big_mac_price_eur = 4.27
    if moeda == 1:
        if quant >= big_mac_price_eur:
            print("Sim, é suficiente para comprar um Big Mac!")
        else:
            print("Não, não é suficiente para comprar um Big Mac.")
    elif moeda == 2:
        if quant >= big_mac_price_eur / 1.17:
            print("Sim, é suficiente para comprar um Big Mac!")
        else:
            print("Não, não é suficiente para comprar um Big Mac.")
    elif moeda == 3:
        if quant >= big_mac_price_eur / 6.37:
            print("Sim, é suficiente para comprar um Big Mac!")
        else:
            print("Não, não é suficiente para comprar um Big Mac.")
    if quant or quant1 or quant2 <= 0:
     print("Quantia inválida.")

if str(input()) == "4":
    print("Qual a moeda que vais utilizar:")
    print("1- EUR")
    print("2- USD")
    print("3- BRL")
    moeda = int(input())
    print("Insira a sua quantia:")
    quant = float(input())
    print("Quantos dias pretendes simular?")
    dias = int(input())
    quantfinal = float(quant * (int(dias // 2)))
    if moeda == 1:
        print(f"No final de {dias} dias, você terá {quantfinal} EUR.")
    elif moeda == 2:
        print(f"No final de {dias} dias, você terá {quantfinal} USD.")
    elif moeda == 3:
        print(f"No final de {dias} dias, você terá {quantfinal} BRL.")
    if quant or quant1 or quant2 <= 0:
     print("Quantia inválida.")

if str(input()) == "5":
    print("Sair do programa. Até à próxima!")