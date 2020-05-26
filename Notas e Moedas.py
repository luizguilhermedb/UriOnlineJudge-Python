valor = float(input())
valor = round(valor,2)
if valor >= 0 and valor <= 1000000.00:

    i = 0

    cem = 100.00
    cinquenta = 50.00
    vinte = 20.00
    dez = 10.00
    cinco = 5.00
    dois = 2.00

    Mum = 1
    Mcinquenta = 0.50
    Mvintecinco = 0.25
    Mdez = 0.10
    Mcinco = 0.05
    Mumcent = 0.01

    while valor >= cem:
        valor = valor - cem
        i += 1
    print ("NOTAS:")
    print (i, "nota(s) de R$ 100.00")
    i = 0
    valor = round(valor,2)

    while valor >= cinquenta:
        valor = valor - cinquenta
        i += 1
    print (i, "nota(s) de R$ 50.00")
    i = 0
    valor = round(valor,2)

    while valor >= vinte:
        valor = valor - vinte
        i += 1
    print (i, "nota(s) de R$ 20.00")
    i = 0
    valor = round(valor,2)

    while valor >= dez:
        valor = valor - dez
        i += 1
    print (i, "nota(s) de R$ 10.00")
    i = 0
    valor = round(valor,2)

    while valor >= cinco:
        valor = valor - cinco
        i += 1
    print (i, "nota(s) de R$ 5.00")
    i = 0
    valor = round(valor,2)

    while valor >= dois:
        valor = valor - dois
        i += 1
    print (i, "nota(s) de R$ 2.00")
    i = 0
    valor = round(valor,2)

    while valor >= Mum:
        valor = valor - Mum
        i += 1
    print ("MOEDAS:")
    print (i, "moeda(s) de R$ 1.00")
    i = 0
    valor = round(valor,2)

    while valor >= Mcinquenta:
        valor = valor - Mcinquenta
        i += 1
        valor = round(valor,2)
    print (i, "moeda(s) de R$ 0.50")
    i = 0
    

    while valor >= Mvintecinco:
        valor = valor - Mvintecinco
        i += 1
        valor = round(valor,2)
    print (i, "moeda(s) de R$ 0.25")
    i = 0
    

    while valor >= Mdez:
        valor = valor - Mdez
        i += 1
        valor = round(valor,2)
    print (i, "moeda(s) de R$ 0.10")
    i = 0

    while valor >= Mcinco:
        valor = valor - Mcinco
        i += 1
        valor = round(valor,2)
    print (i, "moeda(s) de R$ 0.05")
    i = 0

    while valor >= Mumcent:
        valor = valor - Mumcent
        i+= 1
        valor = round(valor,2)
    print (i, "moeda(s) de R$ 0.01")
