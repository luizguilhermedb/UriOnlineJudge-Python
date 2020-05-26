quant = 0
lista = []
print("Digite todos os nomes dando apenas espaço")
nomes = input()
lista = nomes.split()

while quant < len(lista):

    
    print("<item>",end="")
    print(lista[quant],end="")
    print("</item>")

    quant += 1
    
