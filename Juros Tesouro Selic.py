tempo = int(input("Digite quantos anos: "))
dinheiro = int(input("Aplicação Mensal: "))

ano = 12
i = 1
valor = 0
j=1

while j <= tempo:
    while i <= 12:
        if valor == 0:
            valor = (dinheiro*0.0054)+ dinheiro
        else:
            valor = valor + dinheiro
            valor = (valor*0.0054)+ valor

        i += 1
    j += 1
    i = 1

print("O valor final é: ", valor)
juros = valor - (tempo*12*dinheiro)
print("Juros ganhos: ", juros)
