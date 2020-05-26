Valor = int(input())
x = Valor
notaCem = 0
notaCin = 0
notaVin = 0
notaDez = 0
notaCinco = 0
notaDois = 0
notaUm = 0

if Valor < 0 or Valor > 1000000:
    print("Presentation Error")

else:
    while Valor > 0:
        Valor = Valor - 100
        notaCem = notaCem + 1
    if Valor < 0:
        Valor = Valor+100
        notaCem = notaCem - 1
        
    while Valor > 0:
        Valor = Valor - 50
        notaCin = notaCin + 1
    if Valor < 0:
        Valor = Valor+50
        notaCin = notaCin - 1

    while Valor > 0:
        Valor = Valor - 20
        notaVin = notaVin + 1
    if Valor < 0:
        Valor = Valor+20
        notaVin = notaVin - 1
        
    while Valor > 0:
        Valor = Valor - 10
        notaDez = notaDez + 1
    if Valor < 0:
        Valor = Valor+10
        notaDez = notaDez - 1

    while Valor > 0:
        Valor = Valor - 5
        notaCinco = notaCinco + 1
    if Valor < 0:
        Valor = Valor+5
        notaCinco = notaCinco - 1

    while Valor > 0:
        Valor = Valor - 2
        notaDois = notaDois + 1
    if Valor < 0:
        Valor = Valor+2
        notaDois = notaDois - 1

    while Valor > 0:
        Valor = Valor - 1
        notaUm = notaUm + 1
    
    print(x)
    print(notaCem,"nota(s) de R$ 100,00")
    print(notaCin,"nota(s) de R$ 50,00")
    print(notaVin,"nota(s) de R$ 20,00")
    print(notaDez,"nota(s) de R$ 10,00")
    print(notaCinco,"nota(s) de R$ 5,00")
    print(notaDois,"nota(s) de R$ 2,00")
    print(notaUm,"nota(s) de R$ 1,00")
