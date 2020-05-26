from random import*
print("Digite 0 pra fechar")
quant = 1

while quant != 0:

    quant = int(input("Digite quantos numeros serão sorteados: "))

    i = quant
    lista = []
    
    while i > 0:
        num = randint(1,quant)
    
        while num in lista:
            num = randint(1,quant)
        
        else:
            lista.append(num)
            i = i - 1
            print("<item>",end="")
            print(num,end="")
            print("</item>")
